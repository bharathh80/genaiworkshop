from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from pydantic import BaseModel

# Specify where the documents are located
directory = './docs'


def load_docs(_directory):
    loader = DirectoryLoader(_directory)
    _documents = loader.load()
    return _documents


def split_docs(_documents, chunk_size=1000, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(_documents)
    return docs


def create_embeddings(_chunks):
    modelPath = "sentence-transformers/all-MiniLM-l6-v2"
    model_kwargs = {"device": "cpu"}
    encode_kwargs = {"normalize_embeddings": False}

    embeddings = HuggingFaceEmbeddings(
        model_name=modelPath,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs,
    )
    return embeddings


if __name__ == "__main__":
    documents = load_docs(directory)
    print(f"Number of documents ingested: {len(documents)}")
    chunks = split_docs(documents)
    print(f"Number of chunks created: {len(chunks)}")
    embedding = create_embeddings(chunks)

    try:
        # Creating a vector store
        db = FAISS.from_documents(chunks, embedding)
        db.save_local(folder_path="../database/faiss_db", index_name="myFaissIndex")
        print("FAISS index created")

        # Loading the index for searching
        db = FAISS.load_local(folder_path="../database/faiss_db", embeddings=embedding, index_name="myFaissIndex")
        searchDocs = db.similarity_search("What is the return policy for?")
        print(searchDocs[0].page_content)
    except Exception as e:
        print(e)
        print("FAISS index creation failed")