
# CodeFlow AI
### AI-Powered Security Auditor & System Architecture Visualizer
 
> **Transform raw backend code into security intelligence and interactive architecture diagrams — in real time.**
 
---
 
## 🏆 AMD Hackathon (lablab.ai) — AUREX AI Labs
 
---
 
## What is CodeFlow AI?
 
CodeFlow AI is an AI-powered platform that automatically analyzes backend source code, detects security vulnerabilities, and generates interactive system architecture diagrams — all in one unified dashboard.
 
No manual documentation. No missed vulnerabilities. Just **clear, secure, visual intelligence**.
 
---
 
## The Problem
 
Modern backend systems suffer from:
 
- Hidden security vulnerabilities (SQL Injection, XSS, hardcoded secrets, broken auth)
- Zero documentation on legacy codebases
- Hours wasted manually tracing system architecture
- Critical bugs caught too late in the development cycle
---
 
## Our Solution
 
CodeFlow AI automates the entire backend analysis pipeline:
 
```
Developer uploads code
        ↓
Code Ingestion & AST Parsing
        ↓
AI Analysis — Llama 3 on AMD Cloud (vLLM)
        ↓
Security Detection Engine
        ↓
Risk Classification (🔴 Red / 🟡 Yellow / 🟢 Green)
        ↓
Architecture Extraction
        ↓
Mermaid.js Diagram Generation
        ↓
Interactive Dashboard with AI Recommendations
```
 
---
 
## 🚦 Security Model
 
| Zone | Meaning | Action |
|------|---------|--------|
| 🔴 **Red** | Critical vulnerability | Immediate fix required |
| 🟡 **Yellow** | Warning-level issue | Review recommended |
| 🟢 **Green** | Safe component | No action needed |
 
---
 
## Core Features
 
**AI Code Analysis**
Deep understanding of backend logic — API flows, database interactions, and authentication patterns analyzed automatically.
 
**Security Detection**
Detects SQL Injection, XSS, hardcoded secrets, broken authentication, and sensitive data exposure.
 
**Architecture Visualization**
Auto-generates system diagrams from code using Mermaid.js — no manual diagramming needed.
 
**Unified Dashboard**
Real-time vulnerability reports, architecture diagrams, and AI-generated fix recommendations in one place.
 
---
 
## Technology Stack
 
| Layer | Technologies |
|-------|-------------|
| Frontend | React.js, Vite, Axios |
| Backend | FastAPI, Node.js, Express.js |
| AI Engine | Llama 3, vLLM |
| Infrastructure | AMD Developer Cloud |
| Visualization | Mermaid.js |
 
---
 
## Getting Started
 
```bash
# Clone the repo
git clone https://github.com/aurex-ai-labs/codeflow-ai
 
# Install frontend dependencies
cd frontend
npm install
npm run dev
 
# Install backend dependencies
cd ../backend
pip install -r requirements.txt
uvicorn main:app --reload
```
 
> **Note:** Requires AMD Developer Cloud credentials for AI inference. See `.env.example` for configuration.
 
---
 
## Key Innovation
 
Most security tools just scan for known patterns. CodeFlow AI goes further — it **understands system context**.
 
By combining security analysis, architecture extraction, and AI reasoning in a single pipeline, it gives developers a complete picture: not just *what* is vulnerable, but *where it lives* in the system and *why it matters*.
 
---
 
## Impact
 
- Cuts manual code review time significantly on complex backends
- Detects vulnerabilities early — before production deployment
- Eliminates documentation bottlenecks on legacy systems
- Gives junior developers senior-level system visibility
---
 
## Future Roadmap
 
- [ ] GitHub repository direct integration
- [ ] AI-generated code fix suggestions
- [ ] Multi-language support (Go, Java, Ruby)
- [ ] DevSecOps CI/CD pipeline plugin
---
 
## Team — AUREX AI Labs
 
| Name | Role |
|------|------|
| **Raqeeba Yasin** | Lead Prompt Engineer + Expert Frontend Developer |
| **Saman Shafique** | Frontend Integration Lead |
| **Maimoona** | Backend Logic Developer |
| **Uma Ammara** | DataBase Design & Logic |
| **Syeda Faiza** | AI Infrastructure Engineer |
| **Muhammad Usman** | Creative Lead & Designer |
| **Rimsha Rani** | API Architect |
| **Shaher Bano** | Presentation |

 
---
 
## Hackathon
 
**Event:** AMD Hackathon — lablab.ai  
**Team:** AUREX AI Labs  
**Track:** AI-Powered Developer Tools  
 
---
 
*CodeFlow AI — Security • Architecture • Intelligence, Unified*
