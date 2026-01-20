import requests

url = "https://prod.actioniq.com/app"
response = requests.get(url)

if response.status_code == 200:
    print(response.text)  # This will print the raw HTML content
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")