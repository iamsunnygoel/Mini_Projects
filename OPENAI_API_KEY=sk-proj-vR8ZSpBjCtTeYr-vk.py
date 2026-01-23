
import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")


# Chat input
user_message = "Hello, ChatGPT! What's the capital of Italy?"

# Call the API
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
    messages=[
        {"role": "user", "content": user_message}
    ]
)

# Print response
print("ChatGPT:", response.choices[0].message["content"])
