import models.groq_model as groq_model
from 2_prompt_template import get_prompt
from 3_search_index import perform_search


def get_user_question():
    return input("Enter your question: ")


def rephrase_question(question):
    system_prompt = get_prompt("GROQ_SYSTEM_SIMPLIFY_QUESTION_PROMPT")
    return groq_model.get_response(question, system_prompt)


def query_search_index(question):
    return perform_search(question)


def generate_response(question, answers):
    system_prompt = get_prompt("GROQ_SYSTEM_CUSTOMER_SUPPORT_PROMPT")
    return groq_model.get_response(question + " " + answers, system_prompt)


if __name__ == "__main__":
    question = get_user_question()
    rephrased_question = rephrase_question(question)
    print(f"Rephrased Question: {rephrased_question}")
    answers = query_search_index(rephrased_question)
    response = generate_response(rephrased_question, answers)
    print(f"Response after index search:\n {response}")
