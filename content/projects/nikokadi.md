---
title: "NikoKadi"
date: 2026-05-15
draft: false
github_url: "https://github.com/BethanyJep/NikoKadi"
technologies: ["JavaScript", "Supabase", "Realtime", "GitHub Pages"]
summary: "An online multiplayer version of Kadi, the Kenyan card game, playable with friends from anywhere."
featured: false
---

Kadi is the card game I grew up playing. This is the online version, so a game no longer depends on everyone being in the same room.

## How it plays

Enter a display name, no sign-up required. Create a room to get a six-character code, or join with a friend's. Once two or more players are in, the host starts the game and everyone takes turns playing cards with the board syncing in real time.

## How it is built

| Layer | Technology |
| --- | --- |
| Frontend | Vanilla JS and CSS on GitHub Pages |
| Auth | Supabase anonymous sign-in |
| Database | Supabase Postgres for rooms, players and game state |
| Real-time sync | Supabase Realtime via `postgres_changes` |
| Deployment | GitHub Actions to GitHub Pages |

No framework and no build step. Supabase Realtime carries the multiplayer sync, Row Level Security protects the game state, and the whole thing is a static site — which is the point. A card game with friends should not need a server to babysit.
