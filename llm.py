from groq import Groq

# Put your Groq API key here
client = Groq(api_key="API_KEY = "YOUR_GROQ_API_KEY")

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