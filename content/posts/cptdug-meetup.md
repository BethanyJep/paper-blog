+++
title = 'Cape Town Developer User Group Meetup'
date = 2025-01-31T06:30:17Z
draft = false
+++

> ⛵ The meetup with a view [Cape Town Developer User Group](https://cptmsdug.dev/).
> 

Have you ever attended a meetup with the perfect view of the Atlantic Ocean? Speaking right next to where you board the ferry to the history filled **Robben Island**? Yeah, I never thought I would—but I did. And afterward, I took a boat ride to Robben Island to immerse myself in its history.

### **Session: Building AI Solutions in Azure AI Foundry**

![](https://github.com/BethanyJep/paper-blog/blob/main/public/assets/images/IMG_1410%20(1).jpeg?raw=true)

For this meetup, I stuck to the philosophy: *if it’s not broken, it doesn’t need fixing.* So, [I redelivered the same session](https://github.com/microsoft/aitour-concept-to-creation-ai-studio) I did in Joburg. The difference? **More questions, more interaction, and an even more engaged audience.** Plus, I got the chance to attend my colleagues’ sessions, which was a great learning experience.

This session serves as a perfect introduction to **Azure AI Foundry** and how to build AI solutions. For this blog, I want to focus on one key part of the session—**Retrieval-Augmented Generation (RAG).**

### Retrieval Augmented Generation (RAG)

RAG is a technique that enhances LLM responses by incorporating your own data. Here’s how it works:

![image.png](https://github.com/BethanyJep/paper-blog/blob/main/public/assets/images/image%20(2).png?raw=true)

- **Data Sourcing and Formatting:** Collect and store your data in one location.
    - Depending on its size, you may need to break it into smaller **chunks** a process called **chunking.**
    - To make the data understandable for the model, it must be converted into a numerical format, known as **vectorization.**
    - Once vectorized, a **search index** makes the data easily searchable just like a library catalog.
    - Finally, to ensure relevant results, the retrieved data is **ranked** based on importance.
- **Retrieval:** When a user asks a question, the app searches the database for relevant information.
- **Augmentation:** The retrieved data is added to the prompt to enhance the response.
- **Generation:** The enhanced prompt is fed to the LLM, which generates a more accurate and context-aware response.

![image.png](https://github.com/BethanyJep/paper-blog/blob/main/public/assets/images/image%20(1).png?raw=true)

Sounds simpler now, right? You can learn more about **implementing RAG** in our [**Generative AI for Beginners**](https://github.com/microsoft/generative-ai-for-beginners/tree/main/15-rag-and-vector-databases) course.

### A session this good should be delivered again, right?

And that’s exactly what I did! In the next blog, I’ll share a **live redelivery** of the session so you can learn alongside me. **See you there!**

> **P.S.** The next session is part of the [**Azure AI Fundamentals Series**](https://aka.ms/aifundamentalstraining-blog) on [Microsoft Reactor](https://aka.ms/aifundamentalstraining-reactors) 📺
>