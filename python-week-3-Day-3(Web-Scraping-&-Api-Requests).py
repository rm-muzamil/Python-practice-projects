import requests
from bs4 import BeautifulSoup

# Target website
url = "https://news.ycombinator.com/"

# Mimic a browser (User-Agent)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# Send request with headers
response = requests.get(url, headers=headers)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract titles
titles = soup.find_all("a", class_="title")  # Updated class name

if titles:
    for idx, title in enumerate(titles, 1):
        print(f"{idx}. {title.text}")
else:
    print("No titles found! Website structure might have changed.")
