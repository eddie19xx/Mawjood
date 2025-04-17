import requests
from bs4 import BeautifulSoup
import json

def scrape_site(url, card_selector):
    r = requests.get(url, headers={"User-Agent":"Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")
    items = []
    for card in soup.select(card_selector):
        title = card.select_one(".title").get_text(strip=True)
        price = card.select_one(".price").get_text(strip=True)
        link  = card.select_one("a")["href"]
        items.append({"title": title, "price": price, "url": link, "source": url})
    return items

all_listings = []
# Example: OpenSooq first page
all_listings += scrape_site(
    "https://om.opensooq.com/en/cars-for-sale", 
    ".listing-card"
)

with open("listings.json", "w", encoding="utf-8") as f:
    json.dump(all_listings, f, ensure_ascii=False, indent=2)
