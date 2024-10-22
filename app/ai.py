import openai

openai.api_key = "your_openai_api_key"

def generate_recommendations(prompt: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()
