from groq import Groq

# Put your Groq API key here
client = Groq(api_key="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")

def generate_response(question):
    try:
        chat = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ],
            model="llama-3.1-8b-instant"
        )

        return chat.choices[0].message.content

    except Exception as e:
        return f"AI error: {str(e)}"