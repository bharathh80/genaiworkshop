from groq import Groq

MODEL_NAME = "llama3-70b-8192"


def get_client():
    return Groq()


def get_response(question, system_prompt):
    client = get_client()

    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        response_format={"type": "json_object"},
        stop=None,
    )


    #out = []
    #for chunk in completion:
    #    out.append(chunk.choices[0].delta.content or "")
    print(completion.choices[0].message)
    return completion.choices[0].message
    #return ''.join(out)
