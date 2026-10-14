
from io import BytesIO
import streamlit as st
from pypdf import PdfReader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma


def create_vectorstore(uploaded_files, domain):
    documents = []

    # 1. Read the uploaded files
    for uploaded_file in uploaded_files:
        file_name = uploaded_file.name
        file_bytes = uploaded_file.getvalue()

        if file_name.lower().endswith(".pdf"):
            reader = PdfReader(BytesIO(file_bytes))

            text = "\n".join(
                page.extract_text() or ""
                for page in reader.pages
            )

        elif file_name.lower().endswith(".txt"):
            text = file_bytes.decode("utf-8", errors="replace")

        else:
            continue

        if text.strip():
            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": file_name,
                        "domain": domain
                    }
                )
            )

    if not documents:
        raise ValueError(
            "No readable text found in the uploaded documents."
        )

    # 2. Split documents into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    # 3. Create embeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=st.secrets["GOOGLE_API_KEY"]
    )

    # 4. Store the chunks in Chroma
    # This creates an in-memory vector store for this session's upload.
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vectorstore