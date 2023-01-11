import requests

r = requests.get('https://raw.githubusercontent.com/martinwrudolf/CMPUT-404/main/lab1.py')
print(r.text)
