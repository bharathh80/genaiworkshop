import streamlit as st
from ingest import load_docs, split_docs, create_embeddings
from search_index import perform_search
from simple_prompt import rephrase_question

# Load and ingest documents
documents = load_docs('./docs')
chunks = split_docs(documents)
embeddings = create_embeddings(chunks)

# Create Streamlit UI
st.title('Document Search')
question = st.text_input('Enter your question:')
if st.button('Search') and question:
    rephrased_question = rephrase_question(question)
    results = perform_search(rephrased_question, embeddings)
    st.write(results)
elif st.button('Search') and not question:
    st.write("Please enter a question.")
