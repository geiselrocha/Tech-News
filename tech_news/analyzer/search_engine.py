from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []

    for new in news:
        if title.lower() in new["title"].lower():
            result.append((new["title"], new["url"]))

    return result


# Requisito 8
def search_by_date(date):
    try:
        format_iso = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        news = search_news({"timestamp": format_iso})
        result = []

        for new in news:
            if format_iso in new["timestamp"]:
                result.append((new["title"], new["url"]))

        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    news = search_news({"category": {"$regex": category, "$options": "i"}})

    result = []

    for new in news:
        if category.lower() in new["category"].lower():
            result.append((new["title"], new["url"]))

    return result
