import requests
import json

prompt = input("Enter Prompt Sentence: ")

response = requests.post('https://api.deepai.org/api/text-generator', data={'text': prompt}, headers={'api-key': 'Your Api Key Here'})

jsonResponse = response.json()

text = jsonResponse['output']

print(text)

