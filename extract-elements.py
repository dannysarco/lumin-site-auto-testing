import requests
from bs4 import BeautifulSoup

# Function to fetch and save HTML content
def fetch_and_save_html(url, file_path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers, verify=True)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            html_content = soup.prettify()
            
            # Save to file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(html_content)
            
            print(f"HTML content saved to {file_path}")
        else:
            print(f"Failed to retrieve {url} - Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve {url} - Exception: {str(e)}")

# Usage
url = "https://www.luminsmart.com"
file_path = "luminsmart_homepage.html"
fetch_and_save_html(url, file_path)