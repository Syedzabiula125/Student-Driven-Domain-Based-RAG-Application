import streamlit as st
import base64
from pathlib import Path
from ingestion import create_vectorstore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

st.set_page_config(
    page_title="Student RAG Assistant",
    page_icon="📚",
    layout="wide"
)

def set_background(image_path):
    image_path = Path(image_path)

    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(
            image_file.read()
        ).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:
                linear-gradient(
                    rgba(5, 15, 30, 0.65),
                    rgba(5, 15, 30, 0.65)
                ),
                url("data:image/png;base64,{encoded_image}");

            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        .block-container {{
            padding-top: 2rem;
            padding-bottom: 3rem;
        }}

        h1, h2, h3 {{
            color: white !important;
        }}

        p, label {{
            color: white !important;
        }}

        hr {{
            border-color: rgba(255, 255, 255, 0.3);
        }}

        .stTextInput input {{
            background-color: rgba(255, 255, 255, 0.12) !important;
            color: white !important;
            border-radius: 10px;
        }}

        .stSelectbox > div > div {{
            background-color: rgba(255, 255, 255, 0.12);
            border-radius: 10px;
        }}

        [data-testid="stFileUploader"] {{
            background-color: rgba(255, 255, 255, 0.10);
            border-radius: 12px;
            padding: 10px;
        }}

        .stButton > button {{
            border-radius: 10px;
            font-weight: 600;
        }}

        [data-testid="stExpander"] {{
            background-color: rgba(0, 0, 0, 0.25);
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("assets/rag_background.png")

st.title("📚 Student-Driven RAG Assistant")

st.write(
    "Upload your study documents and ask questions "
    "using Retrieval-Augmented Generation."
)

domain = st.selectbox(
    "Select your domain",
    [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "Generative AI",
        "Other"
    ]
)

if domain == "Other":
    domain = st.text_input("Enter your domain")

uploaded_files = st.file_uploader(
    "Upload your study documents (PDF or TXT)",
    type=["pdf", "txt"],
    accept_multiple_files=True
)

if uploaded_files:
    st.write("### 📄 Uploaded Documents")

    for file in uploaded_files:
        st.write(f"📄 {file.name} — {file.size:,} bytes")

    if st.button("⚙️ Process Documents"):
        try:
            with st.spinner("Processing your documents..."):
                vectorstore = create_vectorstore(
                    uploaded_files,
                    domain
                )

                st.session_state["vectorstore"] = vectorstore
                st.session_state["domain"] = domain

            st.success("✅ Documents processed successfully!")

        except Exception as e:
            st.error(f"Error processing documents: {e}")

st.divider()
st.header("💬 Ask Your Documents")

if "vectorstore" in st.session_state:

    question = st.text_input(
        "Enter your question about the uploaded documents:"
    )

    if st.button("🤖 Get Answer"):

        if question.strip():

            with st.spinner(
                "🔍 Finding information and generating answer..."
            ):

                docs = st.session_state[
                    "vectorstore"
                ].similarity_search(
                    question,
                    k=4
                )

                context = "\n\n".join(
                    doc.page_content
                    for doc in docs
                )

                llm = ChatGoogleGenerativeAI(
                    model="gemini-2.5-flash",
                    temperature=0
                )

                prompt = ChatPromptTemplate.from_template(
                    """
                    You are a helpful study assistant.

                    Answer the question using only the
                    context provided below.

                    Give a clear and well-structured answer.
                    Explain difficult concepts using simple
                    language and examples when appropriate.

                    If the answer is not present in the
                    context, say:

                    "I could not find the answer in the
                    uploaded documents."

                    Do not make up information.

                    Context:
                    {context}

                    Question:
                    {question}

                    Answer:
                    """
                )

                chain = prompt | llm

                response = chain.invoke(
                    {
                        "context": context,
                        "question": question
                    }
                )

                st.subheader("🤖 Answer")
                st.write(response.content)

                with st.expander(
                    "📚 View retrieved document chunks"
                ):
                    for i, doc in enumerate(
                        docs,
                        start=1
                    ):
                        st.markdown(
                            f"**Source {i}**"
                        )
                        st.write(doc.page_content)

        else:
            st.warning("⚠️ Please enter a question.")

else:
    st.info(
        "📂 Please upload and process your documents first."
    )