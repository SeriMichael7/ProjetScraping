Scraping_web/
├── main.py                    # Point d'entrée
├── config.py                  # URL, délai d'attente, sélecteurs CSS
├── requirements.txt           # Dépendances
└── app/
    ├── controllers/
    │   └── scraping_controleur.py   # Chef d'orchestre : lancer_scraping()
    ├── scraper/
    │   ├── driver.py                # Crée le navigateur Chrome
    │   ├── scraping_web.py          # Ouvre la page et retourne le HTML
    │   └── parsing.py               # Extrait nom et prix depuis le HTML
    ├── models/
    │   ├── produit.py               # Classe Produit (nom, prix)
    │   └── depot.py                 # Classe Depot : stocke les produits
    ├── views/
    │   └── affichage.py             # Affiche les résultats
    └── data/                        # Réservé aux données sauvegardées