class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def __repr__(self):
        return f"Produit(nom={self.nom!r}, prix={self.prix!r})"
