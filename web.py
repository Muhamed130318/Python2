import requests

page = requests.get("http://192.168.0.19")
print(page.status_code)


