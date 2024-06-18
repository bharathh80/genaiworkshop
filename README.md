# README

This repository is designed for a workshop that introduces the basics of creating a generative AI application. The workshop is structured in a way that gradually introduces the participants to various aspects of building such an application. Here's a brief overview of each script in the repository and its role in the workshop:

## simple_prompt.py

This script is used to introduce the concept of generating responses using a hosted API. It uses the Groq API to simulate a conversation with a customer service professional from a leading E-Commerce company called AcmeCorp. The script takes a user's question and generates a professional and polite response.

## prompt_template.py

This script is used to demonstrate how to templatize requests. It loads a JSON file containing various prompts and returns the prompt corresponding to a given string. This allows for more dynamic and flexible generation of responses.

## ingest.py

This script is used to introduce the concept of document ingestion and text processing. It loads documents from a specified directory, splits them into chunks, and creates embeddings for each chunk using a pre-trained HuggingFace model. It then creates a FAISS index from these embeddings and saves it to a local directory.

## search_index.py

This script is used to demonstrate how to use the FAISS index created by `ingest.py` to perform similarity searches. It loads a pre-trained HuggingFace model and a FAISS index from a local directory. It then enters a loop where it takes user input, performs a similarity search on the FAISS index using the input, and prints the content of the most similar document.

## query_module.py

This script is used to demonstrate how to a simple classifier that will rephrase the original question and use this along with the search index results to generate an answer to the question based on the search index


# Workshop Structure

1. Introduction to Generative AI and its applications.
2. Demonstration of generating responses using a hosted API with `simple_prompt.py`.
3. Discussion on how to templatize requests with `prompt_template.py`.
4. Introduction to document ingestion, text processing, and creating embeddings with `ingest.py`.
5. Demonstration of how to use a FAISS index to perform similarity searches with `search_index.py`.
6. Demonstrate how to use a classifier and then use this to generate a new answer in `query_module.py`
7. Q&A and wrap-up.

# Usage

Before running the scripts, you need to set an environment variable `GROQ_API_KEY` to your Groq API key. 

For Mac/Linux users, you can do this in the terminal:

```
export GROQ_API_KEY=your_api_key
```

For Windows users, you can do this in the command prompt:

```
set GROQ_API_KEY=your_api_key
```

Replace `your_api_key` with your actual Groq API key.

After setting the environment variable, you'll need to install the required dependencies listed in `requirements.txt`. You can do this with pip:

```
pip install -r requirements.txt
```

Then, you can run each script with Python:

```
python simple_prompt.py
python prompt_template.py
```
...

Please note that these scripts are designed to work together, and some may require the output of others to function correctly. For example, `3_ingest.py` must be run before `4_search_index.py` to create the FAISS index that the latter script loads.

# Contributing

If you'd like to contribute to this project, please feel free to submit a pull request or open an issue. We appreciate your help!

# License

This project is licensed under the terms of the MIT license.
