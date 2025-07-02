+++
title = 'Explore and Evaluate AI  models for free with GitHub Models'
date = 2025-02-24T06:30:17Z
draft = false
tags = ["AI", "GitHub", "tech", "workshop"]
+++

> 🛠 I have the workshop; you just need to try it out and tell me what you think!

I recently converted my workshop from Azure AI to [GitHub Models](https://github.com/marketplace/models), and it will be globally used as [introductory content](https://globalaicommunity.github.io/global-ai-bootcamp-2025/workshops/#interacting-with-multimodal-models-in-github-models-and-microsoft-copilot) for the [Global AI Bootcamps](https://globalai.community/bootcamp) all over the world in ~125 locations. One of the biggest advantages of using GitHub Models is it provides every GitHub user access to some leading models from Azure AI Model Catalog, allowing you to experiment, test and compare models before you get them to production. Another plus of using [GitHub Models](https://github.com/marketplace/models) is you only need to create your personal token to get started and going - no complicated setup, no friction. Using GitHub Models is free until you hit the rate limits of the different models.

![GitHub Models homepage](/assets/images/image%20(11).png)

## Prompt Engineering

> P.S. You can save and share your progress in the playground with presets.
> 

Prompt engineering is the art of creating a prompt to fine tune the model’s response. In GitHub Models, you can interact with models using both text and multimodal prompts. An example is the prompt below to generate marketing message for the image uploaded.

![Model selection](/assets/images/image%20(5).png)

Besides interacting with the models, you can tweak the different parameters and add a system message to nourish your interactions. In the next example, I have added a System Message, and you can see the difference in the response:

![Model playground](/assets/images/image%20(6).png)

On the top right, you will find **Prompt Editor,** where you can iterate through prompts and ensure your prompts are finely tuned, see the example below:

![Code generation](/assets/images/image%20(7).png)

## Compare models

Before choosing a model, you’ll want to compare their outputs to find the best fit. You can do that in GitHub Models using the compare feature. Giving you details such as input tokens, latency and output tokens to be able to make a decision on the model to use:

![API integration](/assets/images/image%20(8).png)

## From Playground to Code

Now that we have explored the components of GitHub Models on the playground, let’s take it up a notch can we generate more lyrics or craft eye-catching marketing copy using code? To move our Lyrics generator, Lyrics Muse from playground to code, we use the **get API key** button and follow the steps to create a personal access token, install dependencies and run our code.

![Rate limits](/assets/images/image%20(9).png)

Once we open up our Codespace, we will need to:

- Add our GitHub Personal Access Token on our terminal as follows: `export: GITHUB_TOKEN="your token here"`
- Open the [`basic.py`](http://basic.py) file using the path: `samples/python/azure_ai_inference/basic.py`
- Update our system message as follows: `You are LyricMuse, a creative and collaborative songwriting assistant. Your role is to help generate compelling, original, and evocative lyrics, while adapting to various musical genres, moods, and themes. Be imaginative, poetic, and authentic in your suggestions, and feel free to offer creative ideas for song structure, rhyme schemes, hooks, verses, and choruses. Provide advice or inspiration for melodies, phrasing, or rhythm if requested. Always prioritize working collaboratively and enhancing the user’s creative vision.`
- Update the user question to: `I want to write an upbeat, energetic pop song about breaking free from fear and embracing self-confidence.`
- Run the file to generate music lyrics as shown below.

![Usage dashboard](/assets/images/image%20(10).png)

## Go forth and conquer!

Nothing is stopping you from testing and experimenting with AI Models. Got an idea you want to implement? [Get started today and do your magic!](https://github.com/marketplace/models)