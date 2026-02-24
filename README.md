# BEARL- Browser Extension , AI Agent , RAG , LLM Framework Detecting Client side web attacks in Real time
Detecting Client Side Web attacks 


🔐 AI-Driven Client-Side Web Vulnerability Detection Using LangChain & Ollama

This project implements an AI-powered client-side web security analysis system that detects DOM-based vulnerabilities, CSRF, clickjacking, and phishing attacks by analyzing a user-provided URL.
The system leverages local LLM inference using Ollama and a Retrieval-Augmented Generation (RAG) pipeline orchestrated through LangChain, ensuring privacy, explainability, and resistance to hallucinations.

🧠 How AI Is Used in This Project

Instead of relying on traditional signature-based scanners, this system treats web security analysis as a reasoning problem.
AI is used to understand page behavior, intent, and risk patterns, not just match rules.

The model reasons over:

DOM structure and JavaScript logic

HTML forms, iframes, and event handlers

URL parameters and redirection behavior

Security headers and browser-side indicators

🧩 Role of LangChain

LangChain is used as the orchestration layer for the entire analysis pipeline:

URL Loader: Fetches and parses HTML content from the target URL

Text Chunking: Splits cleaned HTML/JS into semantically meaningful chunks

Vector Storage (ChromaDB): Stores embeddings for efficient semantic retrieval

Retriever (MMR-based): Selects the most relevant and diverse context for analysis

Prompt Control: Enforces strict system roles (e.g., HTML Security Analyst) to prevent hallucinations

Agent Workflow: Enables multi-step reasoning (WHOIS → HTML → JS → Security inference)

LangChain ensures the LLM only reasons over verified, retrieved content, making the analysis grounded and auditable.

🦙 Role of Ollama (Local LLM)

Ollama is used to run the LLM locally, eliminating reliance on third-party APIs and protecting sensitive browsing data.

The LLM is responsible for:

Identifying DOM-based XSS sinks and sources

Detecting CSRF indicators (missing tokens, unsafe methods)

Analyzing clickjacking risks (iframes, X-Frame-Options absence)

Reasoning about phishing characteristics (form behavior, brand impersonation, redirects)

Producing human-readable security explanations

Because inference is local:

Browser data never leaves the system

The model can be safely integrated into security tools and extensions

The system aligns with zero-trust and privacy-by-design principles

🧪 Retrieval-Augmented Generation (RAG) for Security

To avoid hallucination and improve accuracy, the system uses RAG:

Web content is embedded and stored in ChromaDB

Relevant chunks are retrieved per security question

The LLM analyzes only retrieved evidence

All findings are traceable to actual page content

This makes the AI suitable for security-critical decision making.

🎯 Detected Attack Categories

DOM-Based XSS

CSRF

Clickjacking

Phishing & Malicious Redirects

Unsafe JavaScript Patterns

Missing or Misconfigured Security Headers

🚀 Why This Approach Is Different

✔ Local LLM (privacy-preserving)
✔ URL-centric (no server access required)
✔ Reasoning-based detection (not signature-based)
✔ Explainable findings (security analyst friendly)
✔ Easily extendable to browser extensions and IDS agents
