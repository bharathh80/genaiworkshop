from groq import Groq

MODEL_NAME = "llama3-70b-8192"


def get_client():
    return Groq()


def get_safe_unsafe(question):
    client = get_client()

    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "Act as a guardrail library would for an ecommerce customer "
                "service automated response system."
                "Filter out all input that is objectionable, irrelavant,or politically "
                "sensitive. Reply with the word "
                "unsafe if the content meets the above rules. Reply with the word safe "
                "if the content does not meet the rules."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0,
        max_tokens=1,
        top_p=1,
        stream=True,
        response_format=None,
        stop=None,
    )
    i = 0
    for chunk in completion:
        if i == 0:
            print(chunk.choices[0].delta.content or "")

            return chunk.choices[0].delta.content
        i += 1
        
   
