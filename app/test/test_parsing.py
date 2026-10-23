from app.scraper.parsing import extraire_produits

HTML = """
<div class="a-section octopus-pc-card octopus-best-seller-card">
  <div class="a-section octopus-pc-asin-title">Téléphone X</div>
  <span class="a-price"><span class="a-offscreen">199,99 €</span></span>
</div>
"""


def test_extraire_produits():
    produits = extraire_produits(HTML)
    assert len(produits) == 1
    assert produits[0].nom == "Téléphone X"
    assert produits[0].prix == "199,99 €"
