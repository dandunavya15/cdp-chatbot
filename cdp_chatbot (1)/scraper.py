import requests
from bs4 import BeautifulSoup
import json

CDP_DOCS = {
    "Segment": "https://segment.com/docs/",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

def scrape_docs(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    content = [section.get_text() for section in soup.find_all(["h1", "h2", "p"])]
    return "\n".join(content)

docs_data = {cdp: scrape_docs(url) for cdp, url in CDP_DOCS.items()}

with open("cdp_docs.json", "w") as file:
    json.dump(docs_data, file, indent=4)
