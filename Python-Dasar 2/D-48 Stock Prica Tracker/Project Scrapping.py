import requests
from bs4 import BeautifulSoup
import time



headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Gecko) Chrome/120.0.0.0 Safari/537.36"}

def fetch_page(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch page: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_stock_price(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    html = fetch_page(url)
    if not html:
        return None
    soup = parse_html(html)
    price_tag = soup.find("fin-streamer", attrs={"data-field": "regularMarketPrice", "data-symbol": ticker.upper()})
    if not price_tag:
        price_tag = soup.find("fin-streamer", attrs={"data-field": "regularMarketPrice"})

    if price_tag:
        return price_tag.text or price_tag.get("data-value")
    else:
        print(f"Could not find price for {ticker}")
        return None

def track_stock_price(ticker, interval=60):
    while True:
        price = get_stock_price(ticker)
        if price:
            print(f"Price of {ticker}: {price}")
        time.sleep(interval)

ticker = "AAPL"
track_stock_price(ticker, 10)
#price = get_stock_price(ticker)
#if price:
#    print(f"Price of {ticker}: {price}")

    
