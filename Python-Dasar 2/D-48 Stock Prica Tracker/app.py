import requests

def fetch_page(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch page: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

# ponytail: simple test fetch
if __name__ == "__main__":
    result = fetch_page("https://httpbin.org/get")
    print(result)

