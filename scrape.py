import requests
from recipe_scrapers import scrape_html


class Scraper(object):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }

    @staticmethod
    def scrape(url):
        response = requests.get(url, headers=Scraper.headers)
        return scrape_html(response.text, org_url=url)
