#  NexAI Workspace: Enterprise-Grade AI SaaS

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Space+Grotesk&weight=700&size=38&pause=1000&color=D97706&center=true&vCenter=true&width=800&lines=⚡+NexAI+Workspace;Enterprise-Grade+AI+SaaS;Powered+by+Groq+LPU+%26+Llama-3.1;Built+by+Dimas+Arya+Ramadhan" alt="Typing SVG" />
</div>

<div align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" alt="AI Animation banner" width="100%">
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
