# RAG:
- Retrival Augumented Generation
- it retrives relevent chunkd from a vectorstore based on the question
- these chunks are passed to the embedding model and converted to vectors
- these vectors are stored in the vectorDB
- When the user does a search, the query and the top rsults are fetched from vectorDB and passed to the LLM model

* Raw text -> Chunks
* Chunks -> Embeddings -> Stored in VectorDB
* User question -> Embeddings -> similarity Search
* top chunks + question -> LLM -> Answer

# Questions:

1. What does the text splitter do, and why do we need it?
- Breaks down large documents into managable pieces so they can be embedded, indexed and retrived efficiently

2. What does the embeddings model do? (Conceptually, not implementation detail)
- Converts text into numerical vector representations that capture semantic meaning

3. What is a vector store, and what does similarity search mean here?
- vector store stores the embeddings and allows similarity search, which retrives the most semantically similar chunks to the query embedding.

4. What part of this pipeline would change if we index PDFs instead of a string?
- The intial part of the pipeline where we directly read the text and convert to chunks using text splitter will modify
- We will be using a library to extract data form PDF and will be passed to our 'R' in RAG pipeline.
