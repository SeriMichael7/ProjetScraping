import sys
from app.controllers.scraping_controleur import lancer_application_console

# Assure le bon encodage UTF-8 dans la console Windows (accents, symboles euro, guillemets spéciaux)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

if __name__ == "__main__":
    lancer_application_console()
