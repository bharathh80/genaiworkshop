from groq import Groq

if __name__ == "__main__":
    client = Groq()
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "Play the role of a customer service professional for a leading E-Commerce company called AcmeCorp and analyse a provided question or ticket from a customer. Be as professional and polite as possible when replying to the provided text. Use your best judgement of what a good response will be based on the refund policies of other leading ecommerce companies sucha as Amazon, Flipkart, Walmart"
            },
            {
                "role": "user",
                "content": "How quickly will I get a refund on a product I have returned?"
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")
