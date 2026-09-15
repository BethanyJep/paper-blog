"""Regression checks against Hugo's production output; no third-party packages."""

from html.parser import HTMLParser
from pathlib import Path
import subprocess
import tempfile
import unittest
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.menu_links = []
        self.images = []
        self.headings = []
        self.entries = []
        self.text_parts = []
        self.in_menu = False
        self.heading = None
        self.entry = None
        self.entry_field = None
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "ul" and attrs.get("id") == "menu":
            self.in_menu = True
        if tag == "a":
            self.links.append(attrs)
            if self.in_menu:
                self.menu_links.append(attrs)
        if tag == "img":
            self.images.append(attrs)
        if tag == "h1":
            self.heading = []
        if tag == "li" and "hub-item" in attrs.get("class", "").split():
            self.entry = {"text": [], "title": [], "date": []}
        if self.entry is not None:
            if tag == "h3" and "hub-title" in attrs.get("class", "").split():
                self.entry_field = "title"
            if tag == "span" and "hub-date" in attrs.get("class", "").split():
                self.entry_field = "date"

    def handle_data(self, data):
        self.text_parts.append(data)
        if self.heading is not None:
            self.heading.append(data)
        if self.entry is not None:
            self.entry["text"].append(data)
            if self.entry_field:
                self.entry[self.entry_field].append(data)

    def handle_endtag(self, tag):
        if tag == "ul":
            self.in_menu = False
        if tag == "h1" and self.heading is not None:
            self.headings.append("".join(self.heading).strip())
            self.heading = None
        if tag in ("h3", "span"):
            self.entry_field = None
        if tag == "li" and self.entry is not None:
            self.entries.append({
                key: " ".join(" ".join(value).split())
                for key, value in self.entry.items()
            })
            self.entry = None

    @property
    def text(self):
        return " ".join(" ".join(self.text_parts).split())


class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.output = tempfile.TemporaryDirectory(prefix="paper-blog-test-")
        cls.addClassCleanup(cls.output.cleanup)
        cls.destination = Path(cls.output.name)
        subprocess.run(
            [
                "hugo", "--minify", "--quiet", "--environment", "production",
                "--baseURL", "https://bethany-jep.com/",
                "--destination", str(cls.destination),
            ],
            cwd=ROOT,
            check=True,
        )

    def page(self, route):
        return Page((self.destination / route.strip("/") / "index.html").read_text())

    def test_routes_and_navigation(self):
        for route in (
            "/", "/about/", "/projects/", "/events/", "/exploring/",
            "/archives/", "/newsletter/", "/content/", "/search/",
        ):
            with self.subTest(route=route):
                page = self.page(route)
                self.assertEqual(len(page.headings), 1)
                menu = [urlparse(a["href"]).path for a in page.menu_links]
                self.assertIn("/about/", menu)
                self.assertNotIn("/search/", menu)
        self.assertTrue((self.destination / "index.json").is_file())
        self.assertTrue((self.destination / "index.xml").is_file())

    def test_homepage_links_and_images(self):
        page = self.page("/")
        self.assertNotIn("A curious human. A work in play.", page.text)
        for link in page.links:
            url = urlparse(link.get("href", ""))
            if url.netloc not in ("", "bethany-jep.com") or not url.path:
                continue
            path = self.destination / url.path.lstrip("/")
            self.assertTrue(path.is_file() or (path / "index.html").is_file(), link)
        for image in page.images:
            self.assertTrue(image.get("alt"), image)
            self.assertTrue(image.get("width") and image.get("height"), image)
            self.assertTrue((self.destination / urlparse(image["src"]).path.lstrip("/")).is_file())
        self.assertIn("/about/", [a.get("href") for a in page.links])
        self.assertIn(
            "https://www.linkedin.com/in/bethany-jep/",
            [a.get("href") for a in page.links],
        )

    def test_about_content(self):
        page = self.page("/about/")
        for text in (
            "I’m Bethany Jepchumba.", "Community and leadership",
            "Together For Africa Organization", "AIU TVET", "KamiLimu",
            "Global Mentorship Initiative",
        ):
            self.assertIn(text, page.text)
        for text in (
            "not the whole picture", "Teaching, learning, connecting",
            "oldies feeling of my LiPlay",
            "The person behind the experiments, the teaching, and the little adventures.",
        ):
            self.assertNotIn(text, page.text)

    def test_content_dates_and_links(self):
        page = self.page("/content/")
        dates = {
            "Generative AI for Beginners": "2025",
            "Using GitHub Copilot with Python": "2024",
            "AI for Beginners": "2023",
            "Alliance Girls High School Software Engineering Program": "Ongoing",
            "Biashara Agent Workshop": "Mar - Apr 2026",
            "Foundry Toolkit and Hosted Agents Workshop": "Jul - Sep 2026",
            "Inside Microsoft Foundry QuickStart": "Aug 2026 - Ongoing",
            "What Is Microsoft Foundry Toolkit for VS Code? What's New and How to Get Started": "Aug - Sep 2026",
            "Model Mondays": "2025 - Ongoing",
        }
        for title, date in dates.items():
            with self.subTest(title=title):
                entry = next((e for e in page.entries if e["title"] == title), None)
                self.assertIsNotNone(entry)
                self.assertEqual(date, entry["date"])
        self.assertIn(
            "Host", next(e["text"] for e in page.entries if e["title"] == "Model Mondays")
        )
        urls = [a.get("href") for a in page.links]
        for url in (
            "https://www.youtube.com/watch?v=gF2RMvXput8&list=PLlrxD0HtieHj61bBwrAqd5yHvwjB8s_oz",
            "https://www.youtube.com/watch?v=MJ74JkUMI9Q&list=PLfFkrJrvj_-w",
            "https://developer.microsoft.com/en-us/reactor/series/s-1485/",
        ):
            self.assertIn(url, urls)


if __name__ == "__main__":
    unittest.main()
