import requests
from bs4 import BeautifulSoup

# 🔗 URL of the site to scrape
url = "https://www.valueresearchonline.com/stories/225406/why-many-rs-40-lakh-per-annum-earners-retire-poor/"

# 1. Fetch the page
response = requests.get(url)
response.raise_for_status()  # Fail if there's an HTTP error

# 2. Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# 3. Extract all paragraphs (<p> tags)
paragraphs = soup.find_all("p")

# 4. Write them into a local text file
with open("scraped_content.txt", "w", encoding="utf-8") as f:
    for p in paragraphs:
        text = p.get_text().strip()
        if text:
            f.write(text + "\n\n")

print("✅ Scraped", len(paragraphs), "paragraphs to scraped_content.txt")
