#  NexAI Workspace: Enterprise-Grade AI SaaS

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_LPU-F59E0B?style=for-the-badge&logo=groq&logoColor=white)
![Llama](https://img.shields.io/badge/Meta_Llama_3.1-0466C8?style=for-the-badge&logo=meta)

**NexAI Workspace** is a high-performance, Full-Stack Generative AI SaaS Minimum Viable Product (MVP). Built to demonstrate the extreme inference speed of **Groq's Language Processing Units (LPUs)** combined with the cutting-edge **Llama-3.1-8b-instant** model, this workspace is designed for data analysis, programming assistance, and enterprise-level AI interaction.

Unlike standard Streamlit applications, NexAI features a highly customized, ultra-premium **Espresso & Bronze Glassmorphism UI**, bypassing native frontend limitations to deliver a truly modern SaaS experience.

---

##  Key Features

- **Blazing Fast Inference:** Powered by the Groq API, delivering near-instantaneous token generation.
- **Advanced UI/UX:** Custom CSS implementation featuring mesh gradients, glassmorphism containers, and custom SVG iconography.
- **Secure Authentication:** Mocked secure gateway (for MVP demonstration purposes) to access the main workspace.
- **Dynamic Context Management:** Real-time chat history retention and isolated session states.
- **System Prompt Engineering:** Embedded with a highly specific system persona to ensure output accuracy, professionalism, and a hidden "Easter Egg" creator acknowledgment.
- **API Key Management:** Client-side API key configuration for secure, user-managed authentication with Groq servers.

---

##  Tech Stack

- **Frontend:** Streamlit, HTML5, Advanced Custom CSS (Glassmorphism)
- **Backend:** Python
- **LLM Engine:** Meta Llama-3.1-8b-instant
- **API Provider:** Groq Cloud LPU

---

##  Getting Started

Follow these steps to run the NexAI Workspace on your local machine.

### 1. Clone the Repository
```bash
git clone https://github.com/dimssrmdn01/Gen-AI-SaaS.git
cd Gen-AI-SaaS
```

### 2. Install Dependencies
Ensure you have Python installed, then install the required libraries:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Launch the Streamlit server:
```bash
streamlit run app.py
```

### 4. Configuration
1. Obtain a free API key from [GroqCloud Console](https://console.groq.com/keys).
2. Login to the NexAI UI (use any text for testing).
3. Navigate to 🔑 **API Config** in the sidebar and securely enter your Groq API Key (`gsk_...`).
4. Move to ⚡ **NexAI Chat** and start interacting!

---

##  Easter Egg & System Prompting
This application utilizes System Prompt Engineering to lock the AI into a specific persona. Try asking the AI: *"Siapa penciptamu?"* or *"Siapa tuanmu?"* to trigger a strict override command demonstrating constraint modeling in LLMs.

---

##  About the Author
**Dimas Arya Ramadhan**
Data Science Undergraduate | Institut Teknologi Sumatera (ITERA)

Passionate about data science, quantitative analytics, and building robust AI-driven applications. This project serves as a practical demonstration of integrating state-of-the-art LLMs with custom front-end architectures.

Let's connect and build the future of AI! 🚀
