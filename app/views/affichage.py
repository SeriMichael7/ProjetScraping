def afficher_produits(produits):
    print("Le nombre de produits contenu sur la page est :", len(produits))
    for p in produits:
        print("nom:", p.nom)
        print("prix:", p.prix)
