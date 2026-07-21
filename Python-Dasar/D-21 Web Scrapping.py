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
soup = BeautifulSoup(html_content, "html.parser")

print(soup.h1.text)
print(soup.p.text)



# %% Project Wikipedia Scrapper Article
import requests
from bs4 import BeautifulSoup

# Step 1: Get Wikipedia Article URL
def get_wikipedia_page(topic):
    url = f"https://en.wikipedia.org/wiki/{topic.replace('','_')}"
    reponse = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}. Check the topic and try again")
        return None
    
# Step 2: Extract Article Topic
def get_article_title(soup):
    return soup.find('h1').text


# Step 3: Extract Article Summary
def get_article_summary(soup):
    paragraphs = soup.find_all('p')
    for para in paragraphs:
        if para.text.strip():
            return para.text.strip()
    return "No Summary Found"

# Step 4: Extract Headings
def get_headings(soup):
    headings = [heading.text.strip() for heading in soup.find_all(['h2', 'h3', 'h4'])]
    return headings

# Step 5: Extract Related Links
def get_related_links(soup):
    link = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('/wiki/') and ":" not in href:
            link.append(f"https://en.wikipedia.org{href}")
    return list(set(link))[:5]

# Step 6: Main Program
def main():
    topics = input("Enter a topic to search on Wikipedia: ").strip()
    page_content = get_wikipedia_page(topics)

    if page_content:
        soup = BeautifulSoup(page_content, 'html.parse')
        title = get_article_title(soup)
        summary = get_article_summary(soup)
        headings = get_headings(soup)
        related_links = get_related_links(soup)

        print("\n---- Wikipedia Article Details ----")
        print(f"\nTittle: {title}")
        print(f"\nSummary: {summary}")
        print(("Headings:"))
        for heading in headings[:5]:
            print(f"- {heading}")

        print("\nRelated Links:")
        for link in related_links:
            print(f"- {link}")

# Run Program
if __name__ == "__main program__":
    main()



# %%
