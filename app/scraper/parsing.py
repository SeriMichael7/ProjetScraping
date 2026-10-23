from bs4 import BeautifulSoup
from app.models.produit import Produit


def extraire_produits(html):
    soup = BeautifulSoup(html, "html.parser")
    blocs = soup.select("div._octopus-search-result-card_style_apbSearchResultItem__2-mx4")
    produits = []
    for bloc in blocs:
        titre = bloc.select_one("div[data-cy=title-recipe]")
        nom = titre.get_text(strip=True) if titre else "Nom non disponible"

        bloc_prix = bloc.find("span", class_="a-price")
        prix_tag = bloc_prix.find("span", class_="a-offscreen") if bloc_prix else None
        prix = prix_tag.get_text(strip=True) if prix_tag else "Prix non disponible"

        produits.append(Produit(nom, prix))
    return produits
