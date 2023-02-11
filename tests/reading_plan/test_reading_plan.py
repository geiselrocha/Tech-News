from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
  )  # noqa: F401, E261, E501
from unittest.mock import patch
from pytest import raises

read_mock = [
    {"title": "Python, a linguagem mais quente do momento", "reading_time": 4},
    {"title": "Selenium, BeautifulSoup ou Parsel?", "reading_time": 3},
    {"title": "Pytest + Faker: a combinação poderosa!", "reading_time": 10},
    {"title": "FastAPI e Flask: frameworks para APIs", "reading_time": 15},
    {"title": "A biblioteca Pandas e o sucesso de Python", "reading_time": 12},
    ]

readable_mock = [
    {"unfilled_time": 3, "chosen_news":
        [("Python, a linguagem mais quente do momento", 4),
            ("Selenium, BeautifulSoup ou Parsel?", 3)], },
    {"unfilled_time": 0, "chosen_news":
        [("Pytest + Faker: a combinação poderosa!", 10)], },
    ]

unreadable_mock = [
    ("FastAPI e Flask: frameworks para APIs", 15),
    ("A biblioteca Pandas e o sucesso de Python", 12)
    ]


def test_reading_plan_group_news():
    with patch(
        "tech_news.analyzer.reading_plan.find_news", return_value=read_mock
    ):
        result = ReadingPlanService.group_news_for_available_time(10)
        assert result["readable"] == readable_mock
        assert result["unreadable"] == unreadable_mock
    with raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(0)
