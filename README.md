## Research assistant
This project implements a locally-hosted RAG(Retrieval-Augmented Generation) pipeline designed for analyzing technical documentation. It is tailored for resource-constrained environments.

## Table of Contents
- [Features](#Features)
- [Requirements](#Requirements)
- [Installation](#Installation)
- [Usage](#Usage)
- [Example Output](#Example\output)


## Features
* Uses RAG to ground LLM responses in high-density technical literature, significantly reducing hallucinations.
* Designed for efficient retrieval and inference without cloud API dependency.
* Fully local execution via Ollama; no data leaves the local machine.
* Implements local database persistence for sub-second startup times

## Requirements:
* git
* Ollama [https://ollama.com]
* Python 3.10+ [https://www.python.org/downloads/release/python-3100/]

## Installation
Clone the repository:
```
git clone https://github.com/happla/research-assistant.git
```
Install the dependencies:
```
pip install langchain langchain-community chromadb pypdf sentence-transformers ollama
```
or run the following command in your terminal to ensure your environment is updated:
```
pip install -r requirements.txt
```

## Usage
1. ensure ollama is running and the model is pulled:
```
ollama pull llama3.2:3b
```

2. Place you technical pdf in the project root
3. run the pipeline:
```
python main.py
```
4. Ask questions regarding your documents.

## Example output
<p align="left">
<img src="https://github.com/happla/research-assistant/blob/main/Output.png" width="350" title="output.png">
</p>

### Future improvements
* Add a Gradio or Streamlit UI for a better user experience
* Implement metadata filtering to cite source pages
