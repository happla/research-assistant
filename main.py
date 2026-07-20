"""
Project: Langchain Local Research Agent
Author: Happla
Date: 2026-07-20
License: MIT 

Description: Local RAG pipeline using Ollama, ChromaDB, and HuggingFace.
"""
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama

def initialize_rag():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    vector_store = Chroma(
        persist_directory="./chroma_db", 
        embedding_function=embeddings
    )
    
    if not os.path.exists("./chroma_db") or len(vector_store.get()['ids']) == 0:
        print("Ingesting PDF...")
        loader = PyPDFLoader("art_of_electronics.pdf")
        data = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = text_splitter.split_documents(data)
        vector_store.add_documents(chunks)
        print("Ingestion complete.")
    
    llm = Ollama(model="llama3")
    
    return llm, vector_store

if __name__ == "__main__":
    llm, vector_store = initialize_rag()
    
    # Simple query test
    query = "How do I calculate the gain of a non-inverting op-amp?"
    retriever = vector_store.as_retriever()
    docs = retriever.get_relevant_documents(query)
    
    # Combine context and send to LLM
    context = "\n".join([d.page_content for d in docs])
    prompt = f"Context: {context}\n\nQuestion: {query}"
    
    print(llm.invoke(prompt))
