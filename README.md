<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Space+Grotesk&weight=700&size=38&pause=1000&color=D97706&center=true&vCenter=true&width=800&lines=%E2%9A%A1+NexAI+Workspace;Enterprise-Grade+AI+SaaS;Powered+by+Groq+LPU+%26+Llama-3.1;Built+by+Dimas+Arya+Ramadhan" alt="Typing SVG" />
</div>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1c100b,100:D97706&height=180&section=header&text=NexAI%20Workspace&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=Enterprise-Grade%20AI%20SaaS&descAlignY=58&descSize=18" alt="NexAI Banner" width="100%">
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-1c100b?style=for-the-badge&logo=python&logoColor=D97706">
  <img src="https://img.shields.io/badge/Streamlit-1c100b?style=for-the-badge&logo=streamlit&logoColor=FF4B4B">
  <img src="https://img.shields.io/badge/Groq_LPU-1c100b?style=for-the-badge&logo=groq&logoColor=F59E0B">
  <img src="https://img.shields.io/badge/Meta_Llama_3.1-1c100b?style=for-the-badge&logo=meta&logoColor=0466C8">
</div>

<br>

<div align="center">
  <strong>NexAI Workspace</strong> is a high-performance, Full-Stack Generative AI SaaS Minimum Viable Product (MVP). Built to demonstrate the extreme inference speed of <b>Groq's Language Processing Units (LPUs)</b> combined with the cutting-edge <b>Llama-3.1-8b-instant</b> model.
</div>

<br>

Unlike standard Streamlit applications, NexAI features a highly customized, ultra-premium **Espresso & Bronze Glassmorphism UI**, bypassing native frontend limitations to deliver a truly modern SaaS experience.

<div align="center">

[Overview](#overview) • [Features](#features) • [Tech Stack](#tech-stack) • [Project Structure](#project-structure) • [Getting Started](#getting-started) • [Configuration](#configuration) • [Easter Egg](#easter-egg--system-prompting) • [Author](#about-the-author)

</div>

---

## Overview

NexAI Workspace is designed as a practical demonstration of a production-style Generative AI SaaS product — combining a low-latency inference backend (Groq LPU) with a fully custom frontend built on top of Streamlit. The project focuses on three things: raw inference speed, interface polish, and clean session/state architecture, making it a solid reference implementation for anyone building AI-powered internal tools or MVPs.

---

## Features

| Feature | Description |
|---|---|
| **Blazing Fast Inference** | Powered by the Groq API, delivering near-instantaneous token generation. |
| **Advanced UI/UX** | Custom CSS implementation featuring mesh gradients, glassmorphism containers, and custom SVG iconography. |
| **Secure Authentication** | Mocked secure gateway (for MVP demonstration purposes) to access the main workspace. |
| **Dynamic Context Management** | Real-time chat history retention and isolated session states. |
| **System Prompt Engineering** | Embedded with a highly specific system persona to ensure output accuracy and professionalism. |
| **API Key Management** | Client-side API key configuration for secure, user-managed authentication with Groq servers. |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit, HTML5, Custom CSS (Glassmorphism) |
| Backend | Python |
| LLM Engine | Meta Llama-3.1-8b-instant |
| API Provider | Groq Cloud LPU |

---

## Project Structure

```
Gen-AI-SaaS/
├── app.py                 # Main Streamlit entry point
├── core_agent.py           # Agent / model orchestration logic
├── requirements.txt         # Python dependencies
├── assets/                 # Static assets (icons, images)
└── README.md
```

---

## Getting Started

Follow these steps to run the NexAI Workspace on your local machine.

### Prerequisites
- Python 3.9 or higher
- A free Groq API key ([console.groq.com/keys](https://console.groq.com/keys))

### 1. Clone the Repository
```bash
git clone https://github.com/dimssrmdn01/Gen-AI-SaaS.git
cd Gen-AI-SaaS
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run app.py
```

---

## Configuration

1. Obtain a free API key from the [GroqCloud Console](https://console.groq.com/keys).
2. Log in to the NexAI UI (any text works for testing purposes).
3. Navigate to **API Config** in the sidebar and enter your Groq API Key (`gsk_...`).
4. Move to **NexAI Chat** and start interacting with the assistant.

---

## Easter Egg & System Prompting

This application uses system prompt engineering to lock the AI into a specific persona. Try asking the assistant: *"Siapa penciptamu?"* or *"Siapa tuanmu?"* — this triggers a strict override command that demonstrates constraint modeling in LLMs.

---

## Roadmap

- [ ] Persistent chat history (database-backed)
- [ ] Multi-model selection (Llama, Mixtral, etc.)
- [ ] Proper authentication layer (replace mocked gateway)
- [ ] Deployment guide (Docker / cloud)

---

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or submit an issue via the [GitHub repository](https://github.com/dimssrmdn01/Gen-AI-SaaS).

---

## License

This project is released for educational and portfolio purposes. Add a license file (e.g. MIT) if you intend to distribute or reuse this code.

---

## About the Author

**Dimas Arya Ramadhan**
Data Science Undergraduate 

Passionate about data science, quantitative analytics, and building AI-driven applications. This project serves as a practical demonstration of integrating state-of-the-art LLMs with custom frontend architecture.

<div align="center">
  <a href="https://github.com/dimssrmdn01"><img src="https://img.shields.io/badge/GitHub-1c100b?style=for-the-badge&logo=github&logoColor=white"></a>
  <a href="https://linkedin.com/in/your-linkedin"><img src="https://img.shields.io/badge/LinkedIn-1c100b?style=for-the-badge&logo=linkedin&logoColor=0A66C2"></a>
</div>
