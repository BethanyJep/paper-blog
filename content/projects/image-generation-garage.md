---
title: "Image Generation Garage"
date: 2024-05-31
draft: false
github_url: "https://github.com/BethanyJep/Image-Generation-Garage"
technologies: ["Python", "Flask", "DALL-E", "OpenAI"]
summary: "A Flask app that reimagines Kenyan cities through randomly styled DALL-E prompts."
featured: false
---

A small Flask app that turns the name of a Kenyan city into artwork. You give it a city, it picks a descriptive prompt at random, and DALL-E renders the result.

## The idea

The prompt library is where the personality lives. Nairobi might come back as a surrealist oil painting in cool blues during a thunderstorm, or an abstract digital piece lit by neon, or a photorealistic pencil sketch bathed in golden hour light. Same city, entirely different mood each time.

It started as a way to see how much a single variable — style, palette, lighting, time of day — changes what a model produces from otherwise identical input.

## Under the hood

- **Flask + Flask-RESTful** for the API layer
- **OpenAI DALL-E** for generation
- **Flask-Caching** to memoize repeat prompts and avoid burning through calls
- A rotating list of descriptive prompt templates, each parameterised on the city name
