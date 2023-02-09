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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
