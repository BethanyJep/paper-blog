---
title: "Writing Editor"
date: 2026-08-07
draft: false
demo_url: "https://bethanyjep.github.io/writing-editor/"
github_url: "https://github.com/BethanyJep/writing-editor"
technologies: ["Python", "Microsoft Agent Framework", "Azure OpenAI", "Flask"]
summary: "A multi-agent writing assistant where five specialist agents work as a team, sharing insights and building on each other's findings."
featured: false
---

Most AI writing tools are a single model doing everything at once. This one splits the job across five specialists who actually talk to each other, built on the **Microsoft Agent Framework**.

## The agents

| Agent | What it handles |
| --- | --- |
| **Research** | Background context, related topics, supporting information |
| **Grammar** | Spelling, punctuation, sentence structure, readability |
| **Fact-Check** | Identifies claims, flags statements needing external verification |
| **Audience** | Fit for the target demographic, engagement potential |
| **Style** | Tone and voice consistency, style guide adherence |

## How they collaborate

The interesting part is the three-phase workflow rather than the agent list:

1. **Parallel analysis** — all five agents review the draft simultaneously using `ConcurrentBuilder` fan-out
2. **Team synthesis** — each agent revisits its suggestions in light of what the others found
3. **Unified output** — a Lead Editor agent reconciles everything into one set of recommendations

That middle phase is what stops the output from reading like five disconnected reports stapled together.

## Content-aware by design

Each agent adapts to what you are writing. Grammar is strict for an article and relaxed for a social post. Fact-checking goes deep on articles and lighter on opinion pieces. A video script gets pacing analysis, hook timing and spoken-word grammar rules instead of prose conventions.
