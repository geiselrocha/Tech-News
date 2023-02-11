from tech_news.database import search_news
from collections import Counter


# Requisito 10
def top_5_categories():
    all_news = search_news({})

    result = []

    for new in all_news:
        result.append(new["category"])
    category_counts = Counter(result).most_common()
    categories_sorted = sorted(category_counts, key=lambda x: (-x[1], x[0]))

    return [category[0] for category in categories_sorted[:5]]
