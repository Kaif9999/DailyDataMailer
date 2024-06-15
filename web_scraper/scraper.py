import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def parse_data(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        headlines = soup.find_all('h2', class_='headline')
        return [headline.text for headline in headlines]

    def scrape(self):
        html_content = self.fetch_data()
        if html_content:
            return self.parse_data(html_content)
        return []
