# 📚 Student-Driven Domain-Based RAG Application

An AI-powered **Retrieval-Augmented Generation (RAG)** application that allows students to upload their study materials and ask questions based on the content of their own documents.

The application combines **Streamlit, LangChain, Google Gemini, and vector-based retrieval** to provide domain-focused answers from uploaded study documents.

## 🚀 Project Overview

Students often need to search through multiple study materials to find answers to specific questions. This application simplifies that process by allowing users to upload their study documents and interact with them using natural language.

The application follows a RAG-based workflow:

```text
Study Documents
      ↓
Document Ingestion
      ↓
Text Processing & Chunking
      ↓
Embeddings / Vector Store
      ↓
Similarity Search
      ↓
Relevant Context
      ↓
Google Gemini LLM
      ↓
Generated Answer
```

## ✨ Features

- 📄 Upload multiple **PDF or TXT** study documents
- 🎯 Select a learning domain
- 📚 Supports domains such as:
  - Python
  - Machine Learning
  - Deep Learning
  - NLP
  - Generative AI
  - Other
- ⚙️ Process uploaded documents
- 🔍 Retrieve relevant document chunks using similarity search
- 🤖 Generate answers using **Google Gemini**
- 📖 Display retrieved document chunks as sources
- 💻 Interactive Streamlit interface
- 🎨 Custom background and user interface

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web application interface |
| LangChain | RAG application framework |
| Google Gemini | Large Language Model |
| Vector Store | Document retrieval |
| Similarity Search | Retrieve relevant content |
| PDF/TXT Processing | Document ingestion |

## 📂 Project Structure

```text
Student-Driven-Domain-Based-RAG-Application/
│
├── .streamlit/
│   └── secrets.toml
│
├── assets/
│   └── rag_background.png
│
├── app.py
├── config.py
├── ingestion.py
├── req.txt
├── .gitignore
└── README.md
```

## 🔄 How the Application Works

### 1. Select a Domain

The user selects the relevant learning domain, such as:

```text
Python
Machine Learning
Deep Learning
NLP
Generative AI
```

### 2. Upload Documents

Users can upload multiple PDF or TXT study documents.

### 3. Process Documents

The application processes the uploaded documents and creates a vector-based representation that can be searched efficiently.

### 4. Ask a Question

After processing the documents, the user can enter a question related to the uploaded study material.

### 5. Retrieve Relevant Information

The application performs similarity search and retrieves the most relevant document chunks.

### 6. Generate an Answer

The retrieved context is passed to **Google Gemini**, which generates a clear answer based on the available document context.

### 7. View Sources

The application also allows users to view the retrieved document chunks used to generate the answer.

## 💻 Installation

### Clone the Repository

```bash
git clone https://github.com/Syedzabiula125/Student-Driven-Domain-Based-RAG-Application.git
```

### Navigate to the Project

```bash
cd Student-Driven-Domain-Based-RAG-Application
```

### Create a Virtual Environment

```bash
python -m venv rag
```

Activate it on Windows:

```bash
rag\Scripts\activate
```

### Install Dependencies

```bash
pip install -r req.txt
```

## 🔐 API Configuration

This project uses Google Gemini for answer generation.

Create your environment/Streamlit secret configuration and add your Gemini API key securely.

**Do not upload your API key to GitHub.**

Example:

```text
GOOGLE_API_KEY=your_api_key_here
```

Keep sensitive credentials outside your source code and make sure they are included in `.gitignore`.

## ▶️ Run the Application

Run the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🎯 Use Case

This application can be useful for:

- Students preparing for exams
- Personal study assistants
- Technical documentation Q&A
- Learning from course materials
- Domain-specific knowledge assistants
- Educational GenAI applications

## 🧠 Key Learning Outcomes

Through this project, I gained practical experience with:

- Retrieval-Augmented Generation (RAG)
- Document ingestion
- Text processing
- Embeddings and vector search
- Similarity-based retrieval
- Prompt engineering
- Large Language Models
- Google Gemini integration
- LangChain
- Streamlit application development
- Building an end-to-end Generative AI application

## 🔮 Future Enhancements

Potential improvements include:

- 💬 Chat history and conversational memory
- 📑 Support for additional document formats
- 🔎 Advanced retrieval and reranking
- 📊 RAG evaluation
- 🌐 Deployment on cloud platforms
- 🔐 User authentication
- 📚 Multiple knowledge bases
- 📈 Retrieval and response quality monitoring

## 👨‍💻 Author

**Syed Zabiullah**

GitHub:  
https://github.com/Syedzabiula125

LinkedIn:  
https://www.linkedin.com/in/syed-zabi-802864333

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

### 📌 Project Link

https://github.com/Syedzabiula125/Student-Driven-Domain-Based-RAG-Application
