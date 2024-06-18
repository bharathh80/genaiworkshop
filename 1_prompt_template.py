from models import groq_model
import json


def get_prompt(prompt_str):
    with open("prompts/prompts.json", "r") as f:
        prompts = json.load(f)

        if prompt_str in prompts.keys():
            return prompts[prompt_str]
        else:
            return None


if __name__ == "__main__":
    system_prompt = get_prompt("GROQ_SYSTEM_CUSTOMER_SUPPORT_PROMPT")
    print(groq_model.get_response("How quickly can I get a return for my product?", system_prompt))
