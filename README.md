# BEARL- Browser Extension , AI Agent , RAG , LLM Framework Detecting Client side web attacks in Real time
Detecting Client Side Web attacks 


🔐 AI-Driven Client-Side Web Vulnerability Detection Using LangChain & Ollama

This project implements an AI-powered client-side web security analysis system that detects DOM-based vulnerabilities, CSRF, clickjacking, and phishing attacks by analyzing a user-provided URL.
The system leverages local LLM inference using Ollama and a Retrieval-Augmented Generation (RAG) pipeline orchestrated through LangChain, ensuring privacy, explainability, and resistance to hallucinations.

🧠 How AI Is Used in This Project

The system uses LangChain agents to accept a user-provided URL and fetch content using Python requests and urllib. The extracted HTML and JavaScript are analyzed by a locally hosted LLM via Ollama to identify additional relevant and security-critical content. This processed data is then chunked, embedded, and stored in ChromaDB. Using Retrieval-Augmented Generation (RAG), the most relevant context is retrieved and sent again to the LLM for a final, grounded security decision, enabling detection of DOM-based vulnerabilities, CSRF, clickjacking, phishing indicators, and malicious JavaScript patterns.
