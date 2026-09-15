(() => {
    document.querySelector(".skip-link")?.addEventListener("click", () => {
        document.querySelector("#main-content").focus({ preventScroll: true });
    });
    const motionButton = document.querySelector("#motion-toggle");
    const preference = window.matchMedia("(prefers-reduced-motion: reduce)");
    let paused = preference.matches;

    const setMotion = () => {
        document.body.classList.toggle("motion-paused", paused);
        motionButton.setAttribute("aria-pressed", String(paused));
        motionButton.setAttribute("aria-label", paused ? "Play animations" : "Pause animations");
        motionButton.title = paused ? "Play animations" : "Pause animations";
        motionButton.firstElementChild.textContent = paused ? "▷" : "Ⅱ";
    };

    if (motionButton) {
        document.body.classList.add("motion-ready");
        motionButton.hidden = false;
        setMotion();
        motionButton.addEventListener("click", () => {
            paused = !paused;
            setMotion();
        });
        preference.addEventListener("change", (event) => {
            paused = event.matches;
            setMotion();
        });
    }

    const photos = Array.from(document.querySelectorAll("[data-moment]"));
    const next = document.querySelector("#next-moment");
    const count = document.querySelector("#moment-count");
    if (!photos.length || !next || !count) return;

    let current = 0;
    document.querySelector(".memory-controls").hidden = false;
    next.addEventListener("click", () => {
        photos[current].hidden = true;
        photos[current].classList.remove("developing");
        current = (current + 1) % photos.length;
        photos[current].hidden = false;
        photos[current].classList.add("developing");
        count.textContent = `${current + 1} / ${photos.length}`;
        count.setAttribute("aria-label", `Photo ${current + 1} of ${photos.length}: ${photos[current].querySelector(".handwritten").textContent}`);
    });
})();
