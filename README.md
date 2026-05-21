# langchain_execution-s

# LangChain + LLM Learning Journey
# activliy updation is going on... 
# for full details u can visit indivisual file ,line by line explaination is also there 


**(must visit files -->(pydentic_dempo.py,with_structure_out_json, chat_modlehf.py,with_structureed_output_typed.py))**



## Overview

This project contains my learning journey and practical implementation of Large Language Models (LLMs) using LangChain and Hugging Face. The project covers:

* Open-source and closed-source LLMs
* Chat history management
* Message handling
* Structured output techniques
* Pydantic validation
* JSON parsing

---

# Understanding LLMs

Large Language Models (LLMs) are mainly divided into two categories:

1. Open-source models
2. Closed-source models

I explored and implemented both types. Since I am using free resources, I mostly worked with Hugging Face models.

---

# Hugging Face Model Integration

To use Hugging Face models, I imported models using LangChain integrations.

## Environment Variables

I also learned how to use a `.env` file for storing API tokens securely.

### Important Points

* Tokens should be stored correctly without unnecessary commas or formatting issues.
* Environment variables help keep API keys secure.
* The `dotenv` package is used to load environment variables into the project.

Example:

```env
HF_TOKEN=your_huggingface_token
```

---

# Creating a Basic Chatbot

Initially, I created a simple chatbot using a Hugging Face LLM.

## Problem Identified

The chatbot could not remember previous conversations. Every new query was treated independently.

---

# Implementing Chat History

To solve this issue, I implemented chat history so the model could maintain conversational context.

## Another Problem

Even after implementing history, the messages were not properly labeled:

* Which message belonged to the user
* Which message belonged to the AI

---

# Using Message Classes

To solve the labeling issue, I used message classes provided by LangChain Core.

## Important Message Classes

* `HumanMessage`
* `AIMessage`
* `SystemMessage`

These classes are available in:

```python
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
```

These message classes help structure conversations properly by assigning roles to each message.

After implementing history and message classes, the model was able to understand conversation flow much better.

---

# Structured Output

Later, I explored structured output techniques.

Normally, LLMs return plain text responses. However, when integrating LLMs with applications or systems, responses often need to follow a fixed structure.

Examples:

* JSON
* Dictionaries
* Objects
* Predefined schemas

Structured output is important for:

* APIs
* Databases
* Frontend integrations
* Workflow automation
* System-to-system communication

---

# Structured Output Techniques

I explored three major structured output approaches:

1. Typed Output
2. Pydantic
3. JSON Mode

Each approach has different advantages and use cases.

---

# 1. Typed Output

Typed output is one of the simpler structured output techniques.

## Features

* Define a class/schema
* Ensure structured responses
* Easy to implement

Example use cases:

* Extracting highlighted words
* Returning key themes
* Returning categorized information

Typed output ensures that the model response follows a predefined structure.

---

# 2. Pydantic Structured Output

Pydantic provides advanced validation and schema management.

## Benefits of Pydantic

* Type validation
* Optional fields
* Default values
* Constraints and restrictions
* Automatic error handling
* Better schema control

Using Pydantic, we can:

* Validate LLM responses
* Enforce strict structures
* Define required and optional fields
* Improve reliability of AI applications

---

# 3. JSON Mode

JSON mode forces the model to return responses strictly in JSON format.

## Benefits

* Easy system integration
* Machine-readable output
* Useful for APIs and automation
* Easier parsing and validation

JSON mode is commonly used when structured machine-readable output is required.

---

# Important Limitation

One important limitation discovered during implementation:

## Hugging Face + Pydantic Limitation

Hugging Face models do not fully support:

```python
with_structured_output()
```

with native Pydantic function calling in LangChain.

## Supported Providers

The following providers support native structured output properly:

* OpenAI
* Groq
* Anthropic
* Gemini

## Hugging Face Alternative

For Hugging Face models, structured output is usually implemented using:

* `JsonOutputParser`
* Schema-based prompting

instead of native Pydantic function calling.

---

# Technologies Used

* Python
* LangChain
* Hugging Face
* OpenAI
* Pydantic
* dotenv

---

# Key Learnings

Through this project, I learned:

* How LLMs work
* Difference between open-source and closed-source models
* Chat history implementation
* Message role management
* Structured output handling
* Pydantic validation
* JSON parsing
* Environment variable management
* LangChain integrations

---

