import os
import csv
from bs4 import BeautifulSoup

def load_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

def extract_post(soup):
    posts_data = []
    posts = soup.find_all('div', class_='post')

    for post in posts:
        username = post.find('h2', class_='username').text.strip()
        content = post.find('p', class_='content').text.strip()
        timestamp = post.find('span', class_='timestamp').text.strip()

        posts_data.append({
            'username': username,
            'content': content,
            'timestamp': timestamp
        })
    return posts_data

def save_post_to_csv(posts, output_path):
    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["username", "content", "timestamp"])
        
        for post in posts:
            writer.writerow([post["username"], post["content"], post["timestamp"]])
    print(f"Post saved to {output_path}")

file_path = os.path.join(os.path.dirname(__file__), "social_media.html")
html_content = load_html_file(file_path)

if html_content:
    soup = BeautifulSoup(html_content, 'html.parser')
    posts = extract_post(soup)
    for p in posts:
        print(f"User: {p['username']} | Date: {p['timestamp']}\nContent: {p['content']}\n{'-'*30}")
    
    output_csv = os.path.join(os.path.dirname(__file__), "posts.csv")
    save_post_to_csv(posts, output_csv)
