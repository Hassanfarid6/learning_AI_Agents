// 8-Week Prompt Engineering Developer Plan
// 🗓 Week 1: Understand How LLMs Work

// Goal: Learn how prompts turn into responses.

// Topics

// What are tokens, context, temperature, top-p, max tokens

// Prompt structure: system, user, assistant

// Determinism vs creativity

// Practice

// Use ChatGPT or the OpenAI Playground.

// Try the same prompt with different temperatures (0.2 vs 0.9).

// Observe how tone and style change.

// Mini-Quiz:
// Explain to me next week what “temperature” does, in your own words.

// 🗓 Week 2: Prompt Design Basics

// Goal: Write effective single-prompt instructions.

// Topics

// Role prompts (“Act as…”)

// Task prompts (“Summarize / Explain / Compare…”)

// Output formatting (“Return in JSON / Markdown / Table”)

// Few-shot prompting

// Exercise:
// Write a prompt that summarizes a product review and classifies it as “positive” or “negative.”

// 🗓 Week 3: Structured Reasoning

// Goal: Help the model “think” clearly.

// Topics
// Chain-of-Thought prompting
// Step-by-step reasoning vs direct answers
// Self-consistency prompting
// Mini Project:
// Make a Math Tutor Prompt that guides the model to explain reasoning before the final answer.
// 🗓 Week 4: Frameworks for Agents
// Goal: Understand frameworks that extend reasoning.
// Topics
// ReAct (Reason + Act)
// Tree-of-Thoughts (exploring multiple reasoning paths)
// Reflexion (model improves its own output)
// Mini Project:
// Build a simple Problem Solver script in Node.js that uses ReAct logic.
// 🗓 Week 5: API Integration
// Goal: Use prompts in code.
// Topics
// OpenAI API with Node.js
// Sending structured prompts & parsing responses
// Building prompt templates dynamically
// Mini Project:
// Create a small Prompt Playground in Next.js to test and compare outputs.

// 🗓 Week 6: Advanced Prompt Control

// Goal: Make outputs consistent and machine-readable.

// Topics

// JSON-formatted outputs

// System instructions for tone/style

// Controlling response length & structure

// Mini Project:
// Build a Content Generator app (e.g., product descriptions or blog titles) with a “style selector.”

// 🗓 Week 7: Testing & Evaluation

// Goal: Learn to measure prompt quality.

// Topics

// A/B testing prompts

// Logging outputs

// Building a prompt-testing framework

// Mini Project:
// Make a local web dashboard that records prompts + outputs + ratings.

// 🗓 Week 8: Agentic & RAG-Based Apps

// Goal: Combine everything.

// Topics

// Retrieval-Augmented Generation (RAG) basics

// LangChain or Vercel AI SDK introduction

// Designing multi-prompt pipelines

// Final Project:
// Build your own AI Assistant that answers from uploaded text files or docs using RAG + prompt design.

// 1. Token

// Token aik chhota tukra hota hai text ka — jaise aik word, word ka hissa, ya punctuation mark.
// AI models (jaise ChatGPT) text ko words me nahi, tokens me process karte hain.

// Example:
// Sentence: “I love Pakistan.”
// → Tokens: ["I", " love", " Pakistan", "."] (total 4 tokens)

// 👉 Har model ke paas ek token limit hoti hai (jaise GPT-4 = 128k tokens).
// Is limit me tumhara prompt + AI ka answer dono shamil hote hain.

// 🧩 2. Context

// Context ka matlab hai model ke paas maujood recent conversation ka data —
// yani woh sab text (prompts aur answers) jo model ne ab tak dekha hai.

// Agar context limit khatam ho jaye,
// toh AI purani baatein bhool jata hai (kyunki woh tokens limit se bahar nikal jaati hain).

// Example:
// Agar tum 10 long messages bhej chuke ho, aur model ka limit 8 messages tak ka hai,
// toh sabse purane 2 messages model bhool jaayega.

// 🔥 3. Temperature

// Temperature control karta hai AI ke jawab kitne creative ya random hon.

// Low temperature (0.0–0.3):
// → Stable, predictable, fact-based answers.
// (Example: Coding, legal text, math problems)

// High temperature (0.7–1.0):
// → More creative, expressive, unpredictable answers.
// (Example: Story writing, brainstorming)

// 🎲 4. Top-p (Nucleus Sampling)

// Top-p bhi randomness control karta hai, lekin thoda different tareeke se.
// Yeh model ko kehta hai ke sirf un words me se choose kare jinke combined probability “p” tak hoti hai.

// Example:

// Agar top-p = 1.0 → sab possible words consider karega.

// Agar top-p = 0.5 → sirf top 50% most likely words me se choose karega.

// Usually temperature aur top-p dono ek saath tune karte hain,
// lekin zyada tar ek hi use karte hain.

// 📏 5. Max Tokens

// Yeh setting batati hai ke AI maximum kitne tokens ka answer de sakta hai.

// Agar max_tokens = 100 rakha hai,
// toh AI ka reply 100 tokens (approx. 70–80 words) se zyada nahi hoga.

// Iska use tab hota hai jab tum output length control karna chahte ho.

// 🔹 Ek Simple Summary:
// Term	Meaning (Roman Urdu me)	Control karta hai
// Token	Text ka chhota hissa	Size & cost
// Context	Model ke paas yaad rakha gaya text	Memory / relevance
// Temperature	Randomness (creative ya accurate)	Creativity
// Top-p	Word selection probability	Word diversity
// Max Tokens	Output ki maximum length	Reply ka size
