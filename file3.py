import requests

def correct_transcription_gpt4o(transcript, api_key):
    url = "https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "Correct grammatical mistakes"},
            {"role": "user", "content": transcript}
        ]
    }
    response = requests.post(url, json=data, headers=headers)
    corrected_text = response.json()['choices'][0]['message']['content']
    return corrected_text
