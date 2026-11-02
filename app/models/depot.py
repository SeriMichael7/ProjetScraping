import csv
import os
import sqlite3
from app.models.produit import Produit


def sauvegarder_csv(produits, chemin):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nom", "prix"])
        for p in produits:
            writer.writerow([p.nom, p.prix])


def charger_csv(chemin):
    if not os.path.exists(chemin):
        return []
    produits = []
    with open(chemin, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        lignes = list(reader)
        if len(lignes) > 1:
            for ligne in lignes[1:]:
                if len(ligne) >= 2:
                    produits.append(Produit(ligne[0], ligne[1]))
    return produits



def sauvegarder_sqlite(produits, chemin_db):
    dossier = os.path.dirname(chemin_db)
    if dossier:
        os.makedirs(dossier, exist_ok=True)

    conn = sqlite3.connect(chemin_db)
    try:
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prix TEXT,
                date_scraping TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        cur.executemany(
            "INSERT INTO produits (nom, prix) VALUES (?, ?)",
            [(p.nom, p.prix) for p in produits],
        )
        conn.commit()
    finally:
        conn.close()


def lire_sqlite(chemin_db):
    if not os.path.exists(chemin_db):
        return []
    conn = sqlite3.connect(chemin_db)
    try:
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prix TEXT,
                date_scraping TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        cur.execute("SELECT id, nom, prix, date_scraping FROM produits")
        return cur.fetchall()
    finally:
        conn.close()