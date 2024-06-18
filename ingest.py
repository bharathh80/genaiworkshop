from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings


# Pick the right embedding model to create the vector data store
embeddings = SentenceTransformerEmbeddings(model_name='all-MiniLM-L12-v2')

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
    # Define the path to the pre-trained model you want to use
    modelPath = "sentence-transformers/all-MiniLM-l6-v2"

    # Create a dictionary with model configuration options, specifying to use the CPU for computations
    model_kwargs = {'device': 'cpu'}

    # Create a dictionary with encoding options, specifically setting 'normalize_embeddings' to False
    encode_kwargs = {'normalize_embeddings': False}

    # Initialize an instance of HuggingFaceEmbeddings with the specified parameters
    embeddings = HuggingFaceEmbeddings(
        model_name=modelPath,  # Provide the pre-trained model's path
        model_kwargs=model_kwargs,  # Pass the model configuration options
        encode_kwargs=encode_kwargs  # Pass the encoding options
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
        db = FAISS.load_local(folder_path="../database/faiss_db", embeddings=embeddings, index_name="myFaissIndex")
        searchDocs = db.similarity_search("What is the return policy for?")
        print(searchDocs[0].page_content)
    except Exception as e:
        print(e)
        print("FAISS index creation failed")
