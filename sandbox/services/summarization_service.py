from typing import List, Protocol, Tuple, Literal
from langchain_chroma.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

PERSIST_DIR = "data/chroma"

class LLMClient(Protocol):
    """
        Holds the actual LLM model LLAMA, GPT - Plug and play
        Mainly used for typechecking using protocol to support multiple model.
    """

    def generate(self, prompt: str) -> str:
        ...

class DummyLLMClient:

    def generate(self, prompt: str) -> str:
        lines = prompt.splitlines()
        head = "\n".join(lines[:15])
        return f"[DUMMY SUMMARY]\n\nPrompt head:\n{head}\n\n[...total prompt length={len(prompt)} chars...]"


def get_chunks_for_notes(note_id: str, max_chunks: int = 20):
    
    embeddings = HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")

    vector_db = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function= embeddings
    )
    data = vector_db.get(where = {"note_id": note_id})

    documents = data.get("documents", [])
    metadata = data.get("metadatas", [])
    pairs = list(zip(documents, metadata))

    def sort_pairs(item):
        _, meta = item
        return meta.get("chunk_index") or meta.get("index") or 0
    sorted_pairs = sorted(pairs, key = sort_pairs)

    return sorted_pairs[:max_chunks] if max_chunks is not None else sorted_pairs



def build_summary_report(chunks: List, mode: Literal["short", "detailed"] = "short"):

    if mode == "short":
        instructions = (
            "You are a helpful assistant. Generate a concise high-level summary of the following note."
            "Focus on the main ideas only. Keep it under 5 bullet points."
        )
    elif mode == "detailed":
        instructions = (
            "You are a helpful assistant. Generate a detailed, structured summary of the following note."
            "Include sections like: Overview, Key Concepts, Important Definitions, and Examples if present."
        )    

    joined_content_lines = []
    for text , meta in chunks:
        src = meta.get("source", "unknown")
        idx = meta.get("chunk_index") or meta.get("index") or 0
        joined_content_lines.append(f"[Source:{src} | Chunk: {idx}]\n{text}")
    joined_content = "\n\n".join(joined_content_lines)

    prompt = f"{instructions}\n\n=== NOTE CONTENT START ===\n{joined_content}\n=== NOTE CONTENT END ==="
    
    return prompt

def summarize_notes(note_id: str, llm: LLMClient, mode: Literal["short", "detailed"] = "short", max_chunks = 20):
    
    chunks = get_chunks_for_notes(note_id, max_chunks)
    prompt = build_summary_report(chunks, mode)
    summary = llm.generate(prompt)

    return summary

