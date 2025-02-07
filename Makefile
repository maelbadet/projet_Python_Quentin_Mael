# Variables
PYTEST=pytest

help:
	@echo -e "\033[1;34mMake Commands\033[0m"
	@echo "Usage:"
	@echo "  make [command]"
	@echo -e "\033[1;33mUTILS:\033[0m"
	@echo "  test			Effectue les test unitaires"



# Commande pour exécuter les tests
test:
	$(PYTEST) backend/tests/pytest1.py

# Commande pour vérifier les tests avec des sorties plus détaillées
test-verbose:
	$(PYTEST) -v backend/tests/pytest1.py

# Nettoyer les fichiers temporaires générés (facultatif)
clean:
	find . -type d -name '__pycache__' -exec rm -r {} +; \
	find . -type f -name '*.pyc' -delete