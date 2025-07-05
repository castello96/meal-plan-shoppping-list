import requests
from recipe_scrapers import scrape_html


class Scraper(object):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }

    @staticmethod
    def resolve_redirect(url):
        print(f"Attempting to resolve redirect for url {url}\n")
        try:
            response = requests.get(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
                },
                allow_redirects=True,
                timeout=10,
            )

            print(f"Successfully redirected to {response.url}\n")
            return response.url
        except requests.RequestException as e:
            print(f"Failed to resolve redirect for {url}: {e}")
            return url  # Fallback to original if redirect fails

    @staticmethod
    def scrape(url):
        url = Scraper.resolve_redirect(url)
        response = requests.get(url, headers=Scraper.headers)
        return scrape_html(response.text, org_url=url)
