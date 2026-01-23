from openai import OpenAI

client = OpenAI(api_key="")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain the theory of relativity in simple terms."}
    ]
)   

print(response.choices[0].message.content)