"""
Project: Langchain Local Research Agent
Author: Happla
Date: 2026-07-20
License: MIT 

Description: Local RAG pipeline using Ollama(LLama3), ChromaDB(Vector storage), and HuggingFace(sentence-transformers).
"""
import os
import glob
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama

def initialize_rag():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    persist_dir = "./chroma_db"
    
    db_exists = os.path.exists(persist_dir) and os.path.exists(os.path.join(persist_dir, "chroma.sqlite3"))
    
    vector_store = Chroma(
        persist_directory=persist_dir, 
        embedding_function=embeddings
    )
    
    
    if not db_exists:
        print("Ingesting PDF...")
        pdf_files = glob.glob("*.pdf")
        if not pdf_files:
            print("No pdf files found in the directory.")
            return None, None
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        
        for file_path in pdf_files:
            print(f"Loading: {file_path}")
            loader= PyPDFLoader(file_path)
            data = loader.load()
            chunks = text_splitter.split_documents(data)

            #batching to avoid chromadb limit
            batch_size = 500
            for i in range(0, len(chunks), batch_size):
                batch = chunks[i : i + batch_size]

                vector_store.add_documents(batch)
                print(f"Ingested {len(batch)} chunks from {file_path}")
        
        print("Ingestion complete.")
    else:
        print("Existing database found. Loading from disk..")
    
    llm = Ollama(model="llama3.2:3b")
    return llm, vector_store

if __name__ == "__main__":
    llm, vector_store = initialize_rag()
    # Check if initialization failed
    if llm is None or vector_store is None:
        print("Initialization failed. Exiting.")
        exit()
    retriever = vector_store.as_retriever()

    print("\n--- Research Assistant Ready ---")
    print("Type 'exit' to quit.")
    
    while True:
        # Get user input
        query = input("\nAsk a question about your documents: ")
        
        if query.lower() == "exit":
            break
            
        # Retrieve context
        docs = retriever.invoke(query)
        context = "\n".join([d.page_content for d in docs])
        prompt = f"Context: {context}\n\nQuestion: {query}"
        
        print("Querying the model...")
        try:
            response = llm.invoke(prompt)
            print("\n--- Answer ---")
            print(response)
        except Exception as e:
            print(f"\nError: Could not reach Ollama. Ensure it is running. Details: {e}")
