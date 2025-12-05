import uuid

from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma


PERSIST_DIR = "data/chroma"
PDF_PATH = ""


def read_pdf(path:str):
    loader = PyPDFLoader(path)
    pages = loader.load()
    print(f"Total No. of pages in pdf:{len(pages)}")
    return pages


def split_to_chunks(pages):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 700,
        chunk_overlap = 100,
    )
    chunks = splitter.split_documents(pages)
    print(f"Split the data into {len(chunks)} chunks.")
    return chunks

def embed_and_store(chunks, note_id: str):

    for idx, chunk in enumerate(chunks):
        chunk.metadata["note_id"] = note_id 
        chunk.metadata["chunk_index"] = idx
 
    embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
    vectorDB = Chroma(
        persist_directory= PERSIST_DIR,
        embedding_function= embeddings
    )
    vectorDB.add_documents(chunks)
    # vectorDB.persist()

    print(f"Stored {len(chunks)} chunks in Chroma for note_id={note_id}.")
    
    return vectorDB

def query_note(query, note_id: str):    

    embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

    vectorDB = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function= embeddings
    )

    results = vectorDB.similarity_search_with_score(query, k = 3, filter = {"note_id": note_id})
    print("\n Top results:")
    for doc, score in results:
        print("Content:", doc.page_content)
        print("Metadata:", doc.metadata)
        print(f">>> Score: {score}\n")

if __name__ == "__main__":
    
    FILEPATH = "sandbox/gd.pdf"
    note_id = "920fcc4b-7f4d-4d77-bbd9-41e9776f0832_700_100"#str(uuid.uuid4())

    pages = read_pdf(FILEPATH)
    chunks = split_to_chunks(pages)
    vectorstore = embed_and_store(chunks, note_id) # returned vector store incase we wanted to use the same for query fetching
    
    while True:
        q = input("\nAsk a question (or 'exit'): ")
        if q == "exit":
            break
        query_note(q, note_id)

