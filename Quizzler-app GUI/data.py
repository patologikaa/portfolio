import requests

parameters = {"amount": 10,
              "type": "boolean"}

link = requests.get(url="https://opentdb.com/api.php", params=parameters)
link.raise_for_status()
data = link.json()
question_data = data["results"]