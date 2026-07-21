import requests
import time
from bs4 import BeautifulSoup, FeatureNotFound

# Recommended practice: set a user‑agent and use retries
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

def fetch_with_retry(url, headers, retries=3, delay=2):
    for i in range(retries):
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response
        else:
            print(f"Attempt {i+1} failed with status {response.status_code}")
            time.sleep(delay)
    raise Exception(f"All {retries} attempts failed.")

response = fetch_with_retry(url, headers)

try:
    soup = BeautifulSoup(response.text, "lxml")
except FeatureNotFound:
    soup = BeautifulSoup(response.text, "html.parser")

print(f"Page title: {soup.title.string}")

# %% Kasus 2

from bs4 import BeautifulSoup

html_content = "<h1>Main Title</h1><p> This is paraghrap </p> <a href='https://example.com'>Click Here</a>"
soup = BeautifulSoup(html_content, "hrml.parser")

print(soup.h1.text)
print(soup.p.text)



# %%
