# Application de Gestion des Frais de Mission (FDM)

Application web pour la gestion des frais de mission, développée avec Django.

## Fonctionnalités

- Gestion des missions
- Suivi des frais
- Génération de rapports
- Interface utilisateur intuitive

## Prérequis

- Docker et Docker Compose
- Git

## Installation

1. Clonez le dépôt :
   ```bash
   git clone <url-du-repo>
   cd FDM
   ```

2. Créez un fichier `.env` à la racine du projet avec les variables suivantes :
   ```
   POSTGRES_DB=frais_mission
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   ```

## Utilisation

### Environnement de développement

Pour lancer l'application en mode développement :

```bash
docker-compose up -d
```

L'application sera accessible à l'adresse http://localhost:8000

### Environnement de production

Pour lancer l'application en mode production avec NGINX :

```bash
docker-compose -f docker-compose.prod.yml up -d
```

L'application sera accessible à l'adresse http://localhost

## Architecture

L'application est composée de plusieurs services Docker :

- **web** : Application Django avec Gunicorn
- **db** : Base de données PostgreSQL
- **nginx** : Serveur web NGINX (en production)

## Configuration NGINX

La configuration NGINX se trouve dans le dossier `nginx/`. Elle est utilisée en production pour :

- Servir les fichiers statiques et médias
- Faire office de proxy inverse vers l'application Django
- Gérer les connexions HTTPS (à configurer)

Pour plus d'informations, consultez le [README.md](nginx/README.md) dans le dossier nginx.

## Développement

### Structure du projet

- `frais_app/` : Application Django principale
- `frais_de_mission/` : Configuration du projet Django
- `nginx/` : Configuration NGINX pour la production
- `docker-compose.yml` : Configuration Docker pour le développement
- `docker-compose.prod.yml` : Configuration Docker pour la production

## Licence

[Insérer les informations de licence ici]
