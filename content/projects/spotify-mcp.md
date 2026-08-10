---
title: "Spotify Agent and MCP Server"
date: 2025-07-15
draft: false
github_url: "https://github.com/BethanyJep/llms-and-a-bit-more/tree/main/spotify-play-music"
technologies: ["Python", "MCP", "AI Toolkit", "AppleScript"]
summary: "A Model Context Protocol server that lets an AI agent control Spotify playback on macOS."
featured: false
---

A Model Context Protocol (MCP) server that gives an AI agent hands-on control of Spotify. Instead of asking a chatbot for song recommendations and copying them across yourself, the agent talks to the player directly.

## What it does

- **Music control** — play, pause, skip tracks, and adjust volume
- **AppleScript integration** — drives the native macOS Spotify client, no web API round trip
- **MCP tools** — structured tool definitions any MCP-compatible agent can discover and call
- **Agent Builder** — connects to the AI Toolkit Agent Builder in VS Code for testing

## Why MCP

MCP is what turns "a model that can talk about music" into "an agent that can actually play it." The server exposes each capability as a typed tool, the agent picks the right one from the conversation, and the protocol handles the wiring in between. Swap the agent and the tools still work.

> Source lives in [`spotify-play-music/`](https://github.com/BethanyJep/llms-and-a-bit-more/tree/main/spotify-play-music).
