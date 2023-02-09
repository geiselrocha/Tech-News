import requests
import time
from requests.exceptions import ConnectionError, HTTPError, ReadTimeout
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
            )
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except (ConnectionError, HTTPError, ReadTimeout):
        return None


# Requisito 2
def scrape_updates(html_content):
    try:
        selector = Selector(text=html_content)
        links = selector.css("a.cs-overlay-link::attr(href)").getall()
        return links
    except (HTTPError):
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        selector = Selector(html_content)
        next_page = selector.css("a.next.page-numbers::attr(href)").get()
        return next_page
    except (HTTPError):
        return None


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css("head > link[rel='canonical'] ::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("a.url.fn.n::text").get()
    reading_time = selector.css("li.meta-reading-time::text").get()
    summary = selector.css(
        "div.entry-content > p:nth-of-type(1) ::text").getall()
    category = selector.css("span.label::text").get()

    return {
        "url": url,
        "title": title.rstrip(),
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time.split(" ")[0]),
        "summary": "".join(summary).rstrip(),
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
