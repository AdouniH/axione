# Axitwo API

API FastAPI minimaliste pour la gestion de tickets.

## Prerequis

- Python 3.10+
- Docker + Docker Compose (optionnel)

## Lancer l'application (sans Docker)

Depuis la racine du projet:

```bash
cd axithree
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Application disponible sur:

- API: http://localhost:8000
- Documentation Swagger: http://localhost:8000/docs

## Lancer l'application (avec Docker)

Depuis la racine du projet:

```bash
cd axithree
docker compose up --build
```

Application disponible sur:

- API: http://localhost:8000
- Documentation Swagger: http://localhost:8000/docs


## Lancer les tests unitaires (sans Docker)

Depuis la racine du projet:

```bash
cd axithree
python -m pytest -q
```

## Lancer les tests unitaires (avec Docker)

Depuis la racine du projet:

```bash
cd axithree
docker compose run --rm --build tests
```

## Couverture de code

### Sans Docker

D'abord, installer les dépendances incluant `pytest-cov`:

```bash
pip install -r requirements.txt
```

Puis générer un rapport de couverture de code:

```bash
# Rapport en terminal
pytest --cov=app --cov-report=term-missing

```

### Avec Docker

```bash
# Couverture avec docker-compose
docker compose run --rm tests pytest

# Le rapport HTML est généré dans htmlcov/
```

## Liens utiles

- FastAPI docs locales: http://localhost:8000/docs
- Endpoint tickets: http://localhost:8000/tickets/
