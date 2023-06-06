# Code for sassy chatbot project

import random
import nltk
import spacy
import openai
import requests
from bs4 import BeautifulSoup

nlp = spacy.load('en_core_web_sm-3.1.0')

openai.api_key = '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'

while True:
    user_input = input('You: ')
    if random.random() < 0.1:
        print("Chatbot: I'm not listening to you right now.")
    else:
        doc = nlp(user_input)
        for token in doc:
            if token.pos_ == 'VERB':
                print('Chatbot: That sounds like a great idea!')
                break
        else:
            if 'search for' in user_input:
                query = user_input.replace('search for', '')
                url = f'https://www.google.com/search?q={query}'
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                results = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
                if results:
                    print('Chatbot: ' + results[0].get_text())
                else:
                    print('Chatbot: Sorry, I could not find any results for that search.')
            else:
                response = openai.Completion.create(
                    engine='text-davinci-002',
                    prompt=user_input,
                    max_tokens=60,
                    n=1,
                    stop=None,
                    temperature=0.5,
                )
                print('Chatbot: ' + response.choices[0].text)