import requests

# OpenAI API key
api_key = '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'

def query_openai(prompt):
    """
    Query the OpenAI API with the provided prompt.
    """
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {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}"
    }
    data = {
        "prompt": prompt = "Translate the following English text to French: 'Hello, how are you?'",
        "max_tokens": 150
    }
    response = query_openai(prompt)
print(response)

# Example prompt
prompt = "Translate the following English text to French: 'Hello, how are you?'"
response = query_openai(prompt)
print(response)
