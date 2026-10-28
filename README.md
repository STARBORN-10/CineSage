# 🎬 CineSage — AI-Powered Movie Chatbot

CineSage is an AI-powered movie chatbot built using Python, LangChain, Groq, and Streamlit. It enables users to interact with an AI model through conversational queries and extract structured movie information from text passages.

## ✨ Features

- **AI Chatbot:** Interact with the model using natural language queries.
- **Movie Information Extraction:** Extract details such as movie title, director, release year, and other relevant information from text passages.
- **Structured Output:** Organize extracted information into structured formats using Pydantic.
- **Interactive UI:** Access the application through a simple Streamlit interface.
- **LLM Integration:** Use Groq-powered language models through LangChain.

## 🛠️ Tech Stack

- **Language:** Python
- **LLM Integration:** LangChain, Groq
- **Data Validation:** Pydantic
- **Frontend:** Streamlit
- **Environment Management:** Python dotenv

## 📁 Project Structure

```text
CineSage/
├── app.py             # Streamlit user interface
├── core.py            # Chatbot and extraction logic
├── requirements.txt   # Project dependencies
├── .env               # API key configuration
└── .gitignore         # Files excluded from Git
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CineSage.git
cd CineSage
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from the [Groq Console](https://console.groq.com/).

**Important:** Never upload your `.env` file or expose your API key publicly.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to start using CineSage.

## 🎯 Project Objective

CineSage explores the practical application of Generative AI, prompt engineering, structured data extraction, and large language model integration to build an interactive, text-based movie information assistant.

## 👨‍💻 Author

**Soham Wadekar**

- GitHub: [STARBORN-10](https://github.com/STARBORN-10)
- LinkedIn: [Add your LinkedIn profile](YOUR_LINKEDIN_URL)

---

*Built as a hands-on project while learning Generative AI and LLM application development.*
