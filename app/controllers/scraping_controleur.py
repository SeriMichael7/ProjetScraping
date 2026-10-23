from config import URL, FICHIER_CSV
from app.scraper.scraping_web import recuperer_html
from app.scraper.parsing import extraire_produits
from app.models.depot import sauvegarder_csv
from app.views.affichage import afficher_produits


def lancer_scraping():
    html = recuperer_html(URL)
    produits = extraire_produits(html)
    afficher_produits(produits)
    sauvegarder_csv(produits, FICHIER_CSV)
