---
name: "Bethany Jep — Analogue Field Journal"
description: "Warm paper, forest ink, retro lettering and real moments of a curious life."
colors:
  paper: "#f7f0de"
  sheet: "#fffaf0"
  forest: "#234438"
  ink: "#253d33"
  muted: "#596457"
  tomato: "#70428c"
  pink: "#d5c5e7"
  teaching-bg: "#51365f"
  sky: "#bfd4d7"
  sunflower: "#ebc85b"
  rule: "#d4cfb9"
  code-bg: "#ece5d3"
  code-block-bg: "#23392f"
  print-paper: "#fffbf0"
  button-ink: "#fff6e5"
  together-ink: "#fff5df"
  dark-paper: "#1d2b25"
  dark-sheet: "#273930"
  dark-ink: "#f3ecd9"
  dark-muted: "#c0c8b8"
  dark-tomato: "#d5b2eb"
  dark-rule: "#506053"
  dark-code-bg: "#304239"
  dark-code-block-bg: "#15221b"
typography:
  display:
    fontFamily: "Caprasimo, Georgia, serif"
    fontSize: "clamp(64px, 7.5vw, 96px)"
    fontWeight: 400
    lineHeight: 0.98
    letterSpacing: "-.025em"
  headline:
    fontFamily: "Caprasimo, Georgia, serif"
    fontSize: "clamp(34px, 4.4vw, 49px)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: "-.025em"
  title:
    fontFamily: "Gelasio, Georgia, serif"
    fontSize: "24px"
    fontWeight: 400
    lineHeight: 1.3
  body:
    fontFamily: '"Trebuchet MS", "Segoe UI", sans-serif'
    fontSize: "16px"
    lineHeight: 1.65
  article:
    fontFamily: '"Trebuchet MS", "Segoe UI", sans-serif'
    fontSize: "17px"
    lineHeight: 1.85
  label:
    fontFamily: '"Trebuchet MS", "Segoe UI", sans-serif'
    fontSize: "13px"
    fontWeight: 600
rounded:
  default: "4px"
  action: "3px"
  button: "6px"
  photo: "2px"
  circle: "50%"
spacing:
  page-gutter: "28px"
  mobile-gutter: "22px"
  section: "90px"
  mobile-section: "58px"
  grid-gap: "25px"
  heading-gap: "34px"
components:
  button-primary:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.button-ink}"
    rounded: "{rounded.button}"
    padding: "11px 23px"
  button-light:
    backgroundColor: "{colors.sunflower}"
    textColor: "{colors.forest}"
    rounded: "{rounded.button}"
    padding: "11px 23px"
  search-input:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.default}"
    padding: "15px 20px"
  navigation-link:
    typography: "{typography.label}"
    padding: "10px 0"
  tag:
    backgroundColor: "{colors.code-bg}"
    textColor: "{colors.ink}"
    padding: "4px 10px"
  project-card:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink}"
    padding: "27px"
  instant-photo:
    backgroundColor: "{colors.print-paper}"
    textColor: "{colors.forest}"
    padding: "13px 13px 0"
---

# Design System: Bethany Jep

## Overview

**Creative North Star: "Bethany’s Analogue Field Journal"**

An oldies, instant-photography world inspired by Bethany’s LiPlay: playful, warm,
curious and bold. Butter paper, forest ink, chunky retro lettering, real photographs
and hand-drawn nature make room for teaching, connection, art and adventure.

The interface feels collected rather than corporate. Tilted prints and coloured
notes provide tactile depth; generous whitespace and ruled editorial lists keep
the actual writing comfortable. This documents the finished implementation, not
a proposed redesign or a new aesthetic decision.

**Key Characteristics:**
- Retro display lettering with italic editorial captions.
- Warm paper and forest ink, with plum and lilac accents.
- Real photography, lightly tilted prints and friendly nature drawings.
- Playful details around quiet, usable navigation and long-form writing.

Source of truth: `assets/css/extended/portfolio-personality.css`,
`layouts/index.html`, `layouts/partials/header.html`,
`layouts/partials/doodle.html`, `layouts/partials/moment-image.html` and
`assets/js/personality.js`. Product facts remain in `PRODUCT.md`; page composition
and visitor modes remain in the surface brief.

## Colors

The approved purple palette pairs butter-toned paper and deep botanical greens
with plum, lilac, pale sky and sunflower yellow. Frontmatter values are normative;
the sidecar's generated tonal ramps are preview aids, not additional built tokens.
The existing `tomato` and `pink` token names are retained for compatibility:
they now represent plum accents and lilac paper, respectively.

### Primary
- **Forest:** solid actions and dark lettering on pastel notes.
- **Plum (`tomato`):** the personal greeting, logo detail, links, drawings and focus outlines.
- **Deep plum (`teaching-bg`):** the teaching panel, unchanged between themes.

### Secondary
- **Lilac (`pink`) / Sky:** coloured paper, photo-stack backing and exploration frames.

### Tertiary
- **Sunflower:** playful paper, flower centres and the light action on deep plum.

### Neutral
- **Paper / Sheet:** page canvas and raised content surfaces.
- **Ink / Muted:** reading text and secondary metadata.
- **Rule:** fine separators and restrained borders.
- **Code background / Code-block background:** inline and fenced code surfaces.
- **Print paper / Button ink / Together ink:** deliberately fixed warm lights,
  distinct from the theme-dependent sheet and foreground.

The dark theme replaces paper, sheet, ink, muted, tomato, rule and both code
backgrounds with their `dark-*` values. The dark plum accent is a lighter lilac.
Forest, lilac paper, deep-plum panel, sky, sunflower, print paper,
button ink and together ink do **not** invert. Photographic paper remains light;
pastel notes keep forest text. PaperMod aliases map theme→paper, entry→sheet,
primary/content→ink, secondary→muted and tertiary/border→rule in both themes.

**The Printed Paper Rule.** Keep photographic paper and pastel-note lettering
fixed across themes; only the documented theme-dependent tokens switch.

## Typography

Caprasimo supplies the rounded oldies display voice; Gelasio supplies editorial
titles and italic captions; Trebuchet MS keeps the body friendly and direct.
Fallback stacks are recorded in frontmatter.

- **Display:** the large personal greeting. Most h1/h2 lettering uses Caprasimo
  at normal weight; balanced lines and tight tracking are intentional.
- **Headline:** section headings; interior page titles use
  `clamp(42px, 6vw, 70px)` and article titles `clamp(34px, 5.2vw, 56px)`.
- **Title:** Gelasio journal titles; project titles use 26px, archive titles 22px,
  and article h2s 30px with 1.35 line-height.
- **Body:** base text follows the body token. Articles use the article token,
  with paragraphs and lists limited to 70ch; supporting descriptions range from
  13–17px. There is no single mathematical type scale.
- **Label:** compact navigation; metadata generally uses 11–13px. Buttons use
  14px bold text. Photo counters use tabular numerals.
- **Captions:** Gelasio italic, including 15px instant-print captions and larger
  editorial annotations. Both local font-face declarations load normal 400 TTF
  files with `font-display: swap`; the stylesheet requests italic styling rather
  than declaring a separate italic font file.

**The Quiet Reading Rule.** Reserve the retro display voice for hierarchy; use
the existing body and editorial faces for sustained reading.

## Layout

The main width token is 1100px, navigation width 1200px, with page gutters and
section spacing defined in frontmatter. Layouts alternate paired columns,
three-column note collections and flat ruled lists; article content narrows to
780px. This is a flexible composition vocabulary, not a universal card grid.

At 1100px and below, navigation wraps onto a second row, controls remain beside
the identity, and paired layouts tighten. At 700px and below, page gutters and
section spacing shrink, paired/three-column content becomes single-column, and
navigation links wrap visibly rather than hiding behind a menu. Editorial rows
stack date, title and summary. Articles reduce to 16px text. Mobile print
rotations remain modest and the home photo desk caps at 390px.

## Elevation & Depth

Depth comes from overlapping paper, small rotations, fine borders and selective
shadows, not elevated application chrome. Editorial lists stay flat.

- **Instant print:** `3px 7px 15px #17261c20`.
- **Photo collection print:** `3px 8px 16px #17261c25`.
- **Coloured note:** `2px 4px 0 #23443818`.
- **Landscape print:** `4px 5px 0 #23443815`.
- **Button hover:** `3px 4px 0 var(--tomato)`, paired with
  `translate(-1px, -2px)` and a 0.2s transition.

The photo stack rotates 5deg above lilac and sunflower sheets rotated -12deg and
-6deg. The backing sheets are inset 12px vertically and 18px horizontally so
their rotation does not create horizontal scrolling. Other prints and notes use small, individual tilts. These are material
details, not instructions to rotate every container.

## Shapes

Mostly straight paper edges, thin rules and restrained corner rounding.
Buttons, inputs and small actions use their frontmatter radii. Theme and motion
controls are circular (38px desktop, 34px mobile). The teaching panel has one
generous corner: `7px 70px 7px 7px`, reduced to a 48px top-right corner on mobile.
Image cropping uses square or landscape frames with `object-fit: cover`, not
rounded avatars. Inline flower, sun, camera, leaf, shoe and spark SVGs use
current colour and simple rounded strokes or petal silhouettes.

## Components

### Buttons

Tactile, legible actions: forest with warm-light text, or sunflower with forest
text on the teaching panel. Both have a 48px minimum height and a 1px border.
Hover adds the offset shadow and tiny lift; text colour stays stable on hover
and focus. Smaller demo/repository/event actions use a 36px minimum height,
3px corners and `8px 12px` padding.

Keyboard focus is a 3px plum outline with 6px offset. The teaching panel and
dark-theme pastel notes use sunflower focus outlines. Dark primary buttons
gain rule-coloured borders. Reduced-motion and paused states remove transitions.

### Chips

Event topics/types and project-stack tags are compact labels, not invented
filters: code-background fill, ink text, 1px rule border and 12px type.
No error, disabled or selection variants are defined for these tags.

### Cards / Containers

Project cards use sheet, a 1px rule border and no ambient shadow; featured cards
use sky with forest text. Coloured curiosity notes use the small hard shadow,
subtle border and a ruled footer link. Journal and archive entries use dividers
instead of enclosing every item in a card.

### Inputs / Fields

Search uses sheet, ink text, a 1px ink border and the shared keyboard-focus
treatment. Search results receive thin rule borders. No additional form error
or disabled-state system is established here.

### Navigation

Caprasimo wordmark and flower sit beside compact readable links and explicit
theme/motion controls. Active text receives a 2px plum underline and links
expose `aria-current="page"`. The skip link becomes visible on focus and its
click handler focuses main content. Preserve visible wrapped mobile navigation,
access keys, search, RSS, theme switching and every existing route.

Theme initialization respects the saved `pref-theme` choice or system dark
preference. Decorative drawings are hidden from assistive technology and are
not focusable.

### Instant photographs and motion

Real images sit on fixed warm-white paper with italic captions and meaningful
destination links. The image partial produces 560/1120px-capped WebP candidates,
intrinsic dimensions, responsive sizes and alt text; the first home photo is
eager/high-priority, later images lazy-load.

The camera button advances manually through three photographs, updates a polite
atomic count, and applies an 850ms developing effect with
`cubic-bezier(.16, 1, .3, 1)`. It never auto-advances. A sun rotates over 40s only
after JavaScript enables motion. Motion controls start hidden, reflect pause
state with `aria-pressed`, and track system preference changes; the pause is
not persisted. Reduced-motion CSS suppresses all animation/transitions even if
the play button is pressed. Without JavaScript, the first photograph and its
link remain visible and the unavailable controls stay hidden.

## Do's and Don'ts

### Do:
- **Do** preserve the user-pinned LiPlay/oldies world and playful, warm, curious, bold personality.
- **Do** use real photographs and existing factual captions, with accessible alternative text.
- **Do** keep navigation, reading contrast and long-form typography quieter than the decorative layer.
- **Do** preserve every existing route, search, RSS, theme switching and reduced-motion support.

### Don't:
- **Don't** replace the analogue character with generic corporate portfolio styling.
- **Don't** invert the fixed photographic paper or pastel-note foregrounds in dark theme.
- **Don't** introduce automatic photo rotation or make content depend on animation.
- **Don't** invent testimonials, achievements, events or photographic evidence.
