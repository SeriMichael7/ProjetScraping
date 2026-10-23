import time

from app.scraper.driver import creer_navigateur
from config import DELAI_ATTENTE


def recuperer_html(url):
    navigateur = creer_navigateur()
    try:
        navigateur.get(url)
        time.sleep(DELAI_ATTENTE)
        return navigateur.page_source
    finally:
        navigateur.quit()
