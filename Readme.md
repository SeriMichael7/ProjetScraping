

```text
Scraping_web/
├── main.py                          # Point d'entrée : lance l'application console
├── config.py                        # Paramètres (URL, délais, chemins des fichiers CSV/DB)
├── requirements.txt                 # Dépendances du projet (Selenium, BeautifulSoup4, Pytest)
├── Readme.md                        # Documentation du projet
├── data/                            # Dossier de stockage des données
│   ├── produits.csv                 # Sauvegarde des produits en CSV
│   └── produits.db                  # Sauvegarde des produits en base SQLite
└── app/
    ├── controllers/
    │   └── scraping_controleur.py   # Logique applicative et gestion du menu console
    ├── scraper/
    │   ├── driver.py                # Configuration et instanciation du navigateur Chrome
    │   ├── scraping_web.py          # Chargement de la page et récupération du code HTML
    │   └── parsing.py               # Analyse HTML avec BeautifulSoup et extraction des données
    ├── models/
    │   ├── produit.py               # Classe Produit (nom, prix)
    │   └── depot.py                 # Persistance des données (CSV et SQLite)
    └── views/
        └── affichage.py             # Interface console (menu interactif et affichage des données)
```

---


   ```

---

 Utilisation de l'Application Console

Pour démarrer l'application console, exécutez la commande suivante à la racine du projet :

```bash
python main.py
```

Menu interactif :

Au lancement, le menu suivant s'affiche :

```text
==================================================
        APPLICATION CONSOLE - SCRAPING WEB
==================================================
1. Lancer le scraping (affichage + sauvegarde CSV)
2. Réafficher les derniers produits récupérés
3. Sauvegarder les produits dans la base SQLite
4. Consulter les produits stockés en base SQLite
5. Quitter
==================================================
```

 Description des options :
- **Option 1** : Lance Selenium pour récupérer la page web, extrait les noms et prix des produits avec BeautifulSoup, affiche les résultats dans la console et les sauvegarde dans `data/produits.csv`.
- **Option 2** : Réaffiche immédiatement les produits extraits lors du dernier scraping sans avoir à recharger la page web.
- **Option 3** : Insère les produits récupérés dans la base de données locale `data/produits.db` (SQLite).
- **Option 4** : Affiche tous les produits enregistrés dans la table SQLite avec leur identifiant et date d'enregistrement.
- **Option 5** : Quitte proprement l'application.
