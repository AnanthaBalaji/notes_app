from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter




def search_query(query_list, note_id):

    embedding = HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")

    chroma_db = Chroma(
        persist_directory="data/chroma",
        embedding_function=embedding
    )

    with open(f"920fcc4b-7f4d-4d77-bbd9-41e9776f0832_700_100.txt", "w+") as f:
        for query in query_list:
            f.write("###########################\n")
            f.write(f"##########{query}#########\n")
            f.write("###########################\n\n")

            result = chroma_db.similarity_search_with_score(query, k=3, filter = {
                "note_id":note_id
            })
            result_mmr = chroma_db.max_marginal_relevance_search(query, k = 3, fetch_k = 10, filter = {
                "note_id":note_id
            })


            f.write("========= Dense Semantic Retrival ===========\n\n")
            for doc, score in result:
                f.write(f"Content: {doc.page_content}\n")
                f.write(f"Score:{score}\n")
                f.write("-----------------------\n")
            f.write("=============================================\n\n")

            f.write("========= Maximum Marginal Relavance ===========\n\n")
            for doc in result_mmr:
                f.write(f"Content: {doc.page_content}\n")
                f.write("-----------------------\n")
            f.write("=============================================\n\n")


if __name__ == "__main__":
    search_list = ["gradient descent",
                "optimization algorithm",
                "iterative method for minimizing",
                "Jacques Hadamard",
                "space shuttle propulsion"
    ]
    search_query(search_list, note_id="920fcc4b-7f4d-4d77-bbd9-41e9776f0832_700_100")