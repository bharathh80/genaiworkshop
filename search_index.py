from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# Define the path to the pre-trained model you want to use
modelPath = "sentence-transformers/all-MiniLM-l6-v2"

# Create a dictionary with model configuration options, specifying to use the CPU for computations
model_kwargs = {'device':'cpu'}

# Create a dictionary with encoding options, specifically setting 'normalize_embeddings' to False
encode_kwargs = {'normalize_embeddings': False}

# Initialize an instance of HuggingFaceEmbeddings with the specified parameters
embeddings = HuggingFaceEmbeddings(
    model_name=modelPath,     # Provide the pre-trained model's path
    model_kwargs=model_kwargs, # Pass the model configuration options
    encode_kwargs=encode_kwargs # Pass the encoding options
)

def perform_search(question):
    try:
        db = FAISS.load_local(folder_path="../database/faiss_db",embeddings=embeddings,index_name="myFaissIndex")
        print("Faiss index loaded ")
    except Exception as e:
        print("Fiass index loading failed \n",e)

    searchDocs = db.similarity_search(question)
    return searchDocs[0].page_content

if __name__ == "__main__":
    while True:
        question = input("Enter your query:")
        print(perform_search(question))
