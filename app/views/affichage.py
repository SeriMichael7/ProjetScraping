def afficher_produits(produits):
    print("Le nombre de produits contenu sur la page est :", len(produits))
    for p in produits:
        print("nom:", p.nom)
        print("prix:", p.prix)


def afficher_menu():
    print("\n" + "=" * 50)
    print("        APPLICATION CONSOLE - SCRAPING WEB")
    print("=" * 50)
    print("1. Lancer le scraping (affichage + sauvegarde CSV)")
    print("2. Réafficher les derniers produits récupérés")
    print("3. Sauvegarder les produits dans la base SQLite")
    print("4. Consulter les produits stockés en base SQLite")
    print("5. Quitter")
    print("=" * 50)


def afficher_donnees_sqlite(lignes):
    if not lignes:
        print("\nAucun produit trouvé dans la base de données SQLite.")
        return
    print(f"\nNombre de produits dans la base SQLite : {len(lignes)}")
    print("-" * 50)
    for ligne in lignes:
        id_prod, nom, prix, date_scraping = ligne
        print(f"[{id_prod}] {nom} | Prix: {prix} | Date: {date_scraping}")
    print("-" * 50)

