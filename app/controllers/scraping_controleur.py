from config import URL, FICHIER_CSV, FICHIER_DB
from app.scraper.scraping_web import recuperer_html
from app.scraper.parsing import extraire_produits
from app.models.depot import sauvegarder_csv, sauvegarder_sqlite, lire_sqlite
from app.views.affichage import (
    afficher_produits,
    afficher_menu,
    afficher_donnees_sqlite,
)


def lancer_scraping():
    html = recuperer_html(URL)
    produits = extraire_produits(html)
    afficher_produits(produits)
    sauvegarder_csv(produits, FICHIER_CSV)
    return produits


def lancer_application_console():
    produits_en_memoire = []

    while True:
        afficher_menu()
        choix = input("Votre choix (1-5) : ").strip()

        if choix == "1":
            print("\n[INFO] Lancement du scraping web en cours...")
            try:
                produits_en_memoire = lancer_scraping()
                print(f"\n[SUCCÈS] Scraping terminé ! Données enregistrées dans '{FICHIER_CSV}'.")
            except Exception as e:
                print(f"\n[ERREUR] Une erreur est survenue lors du scraping : {e}")

        elif choix == "2":
            if not produits_en_memoire:
                print("\n[INFO] Aucun produit en mémoire. Lancez d'abord le scraping (option 1).")
            else:
                afficher_produits(produits_en_memoire)

        elif choix == "3":
            if not produits_en_memoire:
                print("\n[INFO] Aucun produit en mémoire. Lancez d'abord le scraping (option 1).")
            else:
                try:
                    sauvegarder_sqlite(produits_en_memoire, FICHIER_DB)
                    print(f"\n[SUCCÈS] {len(produits_en_memoire)} produits sauvegardés dans '{FICHIER_DB}'.")
                except Exception as e:
                    print(f"\n[ERREUR] Erreur lors de la sauvegarde SQLite : {e}")

        elif choix == "4":
            print(f"\n[INFO] Lecture des données depuis '{FICHIER_DB}'...")
            try:
                donnees = lire_sqlite(FICHIER_DB)
                afficher_donnees_sqlite(donnees)
            except Exception as e:
                print(f"\n[ERREUR] Erreur lors de la lecture SQLite : {e}")

        elif choix == "5":
            print("\nFermeture de l'application console. Au revoir !")
            break

        else:
            print("\n[ATTENTION] Choix invalide. Veuillez entrer un chiffre entre 1 et 5.")

