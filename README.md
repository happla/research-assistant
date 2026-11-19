
# Research Assistant

## Project status

This project was developed as an exploration of locally hosted ai and retrieval-augmented generation (rag). while the core functionality demonstrates document retrieval and local llm inference, the implementation uses an older technology stack and would benefit from modernization.

Potential improvements include:

- updating the langchain integration and dependencies.
- modernizing document ingestion and processing.
- improving retrieval quality and evaluation.
- reworking the application architecture for maintainability.
- adding a user interface for document management and interaction.
- improving configuration, error handling, and documentation.

The project serves as an early exploration of local ai systems and provides a foundation for further development.

## Overview

The Research Assistant processes technical documents, extracts and indexes their contents, and retrieves relevant information when answering user queries. By grounding LLM responses in retrieved document context, it aims to improve factual relevance and reduce hallucinations.

All inference and document processing run locally, using Ollama for model management and inference.

## Features

- **Local RAG pipeline** — retrieves relevant document passages to provide context for LLM responses.
- **Local inference** — runs language models through Ollama without cloud API dependencies.
- **Technical document support** — processes PDF documents for knowledge retrieval.
- **Persistent vector storage** — stores embeddings locally to avoid rebuilding the index on every startup.
- **resource-conscious design** — intended for local environments with limited computational resources.
- **privacy-focused** — documents and queries remain on the local machine.

## Architecture

the application follows a basic rag workflow:

1. **document ingestion** — loads technical documents from the project directory.
2. **text processing** — extracts text and divides it into chunks suitable for retrieval.
3. **embedding generation** — converts document chunks into vector representations.
4. **vector storage** — persists embeddings in a local chromadb database.
5. **retrieval** — searches for relevant document chunks based on the user's query.
6. **generation** — provides retrieved context to a local llm through ollama to generate a response.

## Requirements

- git
- python 3.10+
- [ollama](https://ollama.com/)
- a compatible local language model
- sufficient memory and disk space for the selected embedding and generation models

## Installation

clone the repository:

```bash
git clone https://github.com/happla/research-assistant.git
cd research-assistant
```

install the dependencies:

```bash
pip install -r requirements.txt
```

ensure ollama is installed and running.

pull the default language model:

```bash
ollama pull llama3.2:3b
```

## Usage

1. place your technical pdf documents in the designated document directory.
2. ensure ollama is running and the required model is available.
3. start the application:

```bash
python main.py
```

1. ask questions about your indexed technical documentation.

## Example

the following demonstrates an example interaction with the research assistant:

<p align="left">
  <img src="output.png" width="600" alt="research assistant example output">
</p>

## Technology stack

- python
- langchain
- ollama
- chromadb
- sentence transformers
- pypdf

## License

See the repository for license information.
