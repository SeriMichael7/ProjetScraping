import csv
import os


def sauvegarder_csv(produits, chemin):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nom", "prix"])
        for p in produits:
            writer.writerow([p.nom, p.prix])
