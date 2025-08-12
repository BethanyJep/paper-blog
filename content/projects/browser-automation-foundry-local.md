---
title: "Browser Automation with Foundry Local"
date: 2025-06-20
draft: false
github_url: "https://github.com/BethanyJep/Browser-Automation-with-Foundry-Local"
technologies: ["Python", "Flask", "Playwright", "Foundry Local", "AI", "Browser Automation" ]
summary: "An AI-powered browser automation system that uses Foundry Local models."
featured: false
---

This Flask application combines Foundry Local AI models with Playwright browser automation to create intelligent, adaptive web browsing experiences. The system uses AI for dynamic task planning, step-by-step execution, and smart CAPTCHA avoidance.

## 🤖 AI-Driven Intelligence

The core innovation lies in using AI (Phi-3.5 model via Foundry Local) to understand natural language requests and convert them into browser automation workflows. Instead of pre-programmed scripts, the AI dynamically analyzes each task and creates custom execution plans.

### Key AI Features:
- **Dynamic Task Planning**: AI analyzes natural language and creates 4-8 step automation plans
- **Intelligent Action Generation**: Real-time decision making for browser actions based on page context
- **Adaptive Execution**: Smart responses to different website layouts and content
- **Context-Aware Navigation**: AI understands page content to make optimal choices

## Advanced CAPTCHA Protection

One of the standout features is the sophisticated CAPTCHA detection and avoidance system:

- **Multi-Pattern Detection**: Detects various CAPTCHA types (reCAPTCHA, hCAPTCHA, Cloudflare, etc.)
- **Smart Evasion**: Automatically navigates to alternative sites when CAPTCHAs are encountered
- **Keyword Analysis**: Text-based CAPTCHA detection for comprehensive coverage
- **Privacy-Focused Alternatives**: Prefers DuckDuckGo, Bing, StartPage over Google

## Comprehensive Screenshot Documentation

Every automation step is visually documented:
- **Before/After Screenshots**: Complete visual record of the automation process
- **Interactive Web Viewer**: Click to expand screenshots in the browser interface
- **Timestamped Storage**: Organized with unique session IDs
- **Step Descriptions**: AI-generated context for each screenshot

## Example Use Cases

The system can handle complex automation tasks like:
- "Search for Python programming tutorials"
- "Find the latest news about artificial intelligence"
- "Browse Reddit for technology discussions"
- "Look up climate change information on Wikipedia"
- "Check weather forecasts"
- "Find open source projects on GitHub"

Perfect for developers interested in AI-powered automation, local model deployment, and intelligent web scraping without the complexity of cloud-based AI services!
