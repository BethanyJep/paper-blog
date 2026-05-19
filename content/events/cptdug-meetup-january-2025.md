---
title: "Cape Town Developer User Group Meetup"
date: 2025-01-31
upcoming: false
topic: "Building AI Solutions in Microsoft Foundry"
type: "Meetup"
location: "Cape Town, South Africa"
virtual: false
event_url: "https://cptmsdug.dev/"
demo_url: "https://github.com/microsoft/aitour-concept-to-creation-ai-studio"
course_url: "https://github.com/microsoft/generative-ai-for-beginners/tree/main/15-rag-and-vector-databases"
reactor_url: "https://aka.ms/aifundamentalstraining-reactors"
summary: "Delivered Microsoft Foundry session with ocean views at Cape Town Developer User Group with deep dive into RAG."
tags: ["Community", "Speaking", "Microsoft Foundry", "RAG", "Meetup"]
---

An unforgettable meetup experience with the perfect view of the Atlantic Ocean, speaking right next to where you board the ferry to the historically significant Robben Island.

![Meetup photo](/assets/images/IMG_1410%20(1).jpeg)

## Session: Building AI Solutions in Microsoft Foundry

Following the philosophy *"if it's not broken, it doesn't need fixing,"* I redelivered the same session from Johannesburg. However, this experience was enhanced by:

- More questions and interaction
- Even more engaged audience
- Opportunity to attend colleagues' sessions
- Better learning experience overall

The session serves as a perfect introduction to **Microsoft Foundry** and comprehensive AI solution building.

## Deep Dive: Retrieval-Augmented Generation (RAG)

![Microsoft Foundry](/assets/images/image%20(2).png)

Special focus on **RAG,** a technique that enhances LLM responses by incorporating your own data.

### How RAG Works:

- **Data Sourcing and Formatting:** Collect and store your data in one location.
    - Depending on its size, you may need to break it into smaller **chunks** a process called **chunking.**
    - To make the data understandable for the model, it must be converted into a numerical format, known as **vectorization.**
    - Once vectorized, a **search index** makes the data easily searchable just like a library catalog.
    - Finally, to ensure relevant results, the retrieved data is **ranked** based on importance.
- **Retrieval:** When a user asks a question, the app searches the database for relevant information.
- **Augmentation:** The retrieved data is added to the prompt to enhance the response.
- **Generation:** The enhanced prompt is fed to the LLM, which generates a more accurate and context-aware response.

![RAG diagram](/assets/images/image%20(1).png)

Sounds simpler now, right? You can learn more about **implementing RAG** in our [**Generative AI for Beginners**](https://github.com/microsoft/generative-ai-for-beginners/tree/main/15-rag-and-vector-databases) course.

## Resources

- [Session Materials](https://github.com/microsoft/aitour-concept-to-creation-ai-studio)
- [RAG Implementation Guide](https://github.com/microsoft/generative-ai-for-beginners/tree/main/15-rag-and-vector-databases)
- [Azure AI Fundamentals Series](https://aka.ms/aifundamentalstraining-blog)
- [Microsoft Reactor Sessions](https://aka.ms/aifundamentalstraining-reactors)

{{< discord-community >}}