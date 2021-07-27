import requests
import json

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

word = input("შეიტანეთ სათარგმნი სიტყვა: ")
lang = input("რა ენაზე გვსურს თარგმანი? de | ka | ru: ")

payload = f"source=en&target={lang}&q={word}"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "1f77456fcamsh4ff879ab310009bp13f2e9jsna2ba84228f3c",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)
data = json.loads(response.text)
print(data['data']['translations'][0]['translatedText'])