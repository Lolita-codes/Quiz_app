import requests

# Gets questions from the Open trivia database
parameters = {
    'amount': 10,
    'type': 'boolean'
}

response = requests.get(url='https://opentdb.com/api.php', params=parameters)
response.raise_for_status()

question_data = response.json()['results']
