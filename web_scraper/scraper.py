import requests
from bs4 import BeautifulSoup
import logging

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.logger = logging.getLogger(__name__)

    def fetch_data(self):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(self.url, headers=headers)
            response.raise_for_status()
            self.logger.info(f"Fetched data from {self.url} with status code {response.status_code}")
            with open("fetched_content.html", "w", encoding="utf-8") as f:
                f.write(response.text)
            return response.text
        except requests.RequestException as e:
            self.logger.error(f"Error fetching data from {self.url}: {e}")
            return None

    def parse_data(self, html_content):
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            headlines = soup.find_all('h2', class_='headline')
            self.logger.info(f"Found {len(headlines)} headlines")
            if not headlines:
                self.logger.warning("No headlines found.")
            return [headline.text for headline in headlines]
        except Exception as e:
            self.logger.error(f"Error parsing HTML content: {e}")
            return []

    def scrape(self):
        html_content = self.fetch_data()
        if html_content:
            headlines = self.parse_data(html_content)
            self.logger.info(f"Parsed {len(headlines)} headlines.")
            return headlines
        else:
            self.logger.error("Failed to fetch HTML content.")
            return []

# Example main.py to run the scraper

import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting automation suite...")

    # Step 1: Scrape News
    logger.info("Starting web scraping...")
    scraper = WebScraper('https://www.techguidenaveen.com/2024/04/ignou-re-registration-july-2024-session.html#google_vignette')
    headlines = scraper.scrape()
    if headlines:
        logger.info(f"Scraped {len(headlines)} headlines.")
    else:
        logger.error("Failed to scrape headlines.")

if __name__ == "__main__":
    main()
