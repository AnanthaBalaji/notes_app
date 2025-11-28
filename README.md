# Revision App

## Overview:
The app fetches in user notes as input and retrives the topic required for the users revision from a single notes or across all notes.

## Procedure:
The app takes in the notes in the form of document or pdf or python jupyter notebooks and splits them into chunks of data and applies the required preprocessing and stores in Chroma DB. These chunks are passed to the LLAMA model for summarization and given as output to the user. The search is performed either on a particular notes or across all notes. 

## Technologies:

### Model:
Input: Doc, PDF, ipynb(jupyter notebooks)
Storage: Vector DB/ Chroma 
Model: LLAMA(HuggingFace)
Pipeline: RAG and LangChain

### Application:
RestAPI - FastAPI
Storage: Postgres (User information) *
Authentication - JWT*
Output: JSON

* - implemented in later stages.

