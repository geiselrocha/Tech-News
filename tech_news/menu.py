import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title, search_by_date, search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories


def input_news():
    get_tech_news(input("Digite quantas notícias serão buscadas: "))


def input_title():
    search_by_title(input("Digite a título: "))


def input_date():
    search_by_date(input("Digite a data no formato aaaa-mm-dd: "))


def input_category():
    search_by_category(input("Digite a categoria: "))


def top_categories():
    top_5_categories()


def shutdown_script():
    return "Encerrando script"


options = [
        input_news,
        input_title,
        input_date,
        input_category,
        top_categories,
        shutdown_script,
    ]


# Requisitos 11 e 12
def analyzer_menu():
    try:
        menu = input(
            "Selecione uma das opções a seguir:\n"
            " 0 - Popular o banco com notícias;\n"
            " 1 - Buscar notícias por título;\n"
            " 2 - Buscar notícias por data;\n"
            " 3 - Buscar notícias por categoria;\n"
            " 4 - Listar top 5 categorias;\n"
            " 5 - Sair.\n"
        )
        print(options[int(menu)]())
    except Exception:
        sys.stderr.write("Opção inválida\n")
