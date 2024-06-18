import streamlit as st
from ingest import load_docs, split_docs, create_embeddings
from search_index import perform_search
from models import groq_model
from prompt_template import get_prompt

# Load and ingest documents
documents = load_docs('./docs')
chunks = split_docs(documents)
embeddings = create_embeddings(chunks)

# Create Streamlit UI
st.title('Document Search')
question = st.text_input('Enter your question:')
if st.button('Search') and question:
    system_prompt = get_prompt("GROQ_SYSTEM_SIMPLIFY_QUESTION_PROMPT")
    simplified_question = groq_model.get_response(question, system_prompt)
    rephrased_question = groq_model.get_response(simplified_question, system_prompt)
    results = perform_search(rephrased_question, embeddings)
    st.write(results)
elif st.button('Search') and not question:
    st.write("Please enter a question.")
