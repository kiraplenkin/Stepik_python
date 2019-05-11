import requests

with open('dataset_24476_3.txt', 'r') as file:
    for number in file:
        number = number.strip()

        API_URL = 'http://numbersapi.com/{}/math'.format(number)

        res = requests.get(API_URL)

        if 'unremarkable' in res.text:
            print('Boring')
        elif 'boring' in res.text:
            print('Boring')
        elif 'uninteresting' in res.text:
            print('Boring')
        elif 'is a number for which' in res.text:
            print('Boring')
        else:
            print('Interesting')
