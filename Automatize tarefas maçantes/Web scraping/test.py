import requests

res = requests.get('https://bastteeer.com/')


res.raise_for_status()
