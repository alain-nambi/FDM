# Configuration NGINX pour l'application FDM

Ce dossier contient la configuration NGINX pour servir l'application Django FDM en production.

## Structure des fichiers

- `Dockerfile` : Configuration pour construire l'image NGINX
- `nginx.conf` : Configuration principale de NGINX
- `conf.d/app.conf` : Configuration spécifique à l'application FDM
- `logs/` : Dossier pour stocker les logs NGINX

## Fonctionnalités

- Servir les fichiers statiques et médias
- Proxy inverse vers l'application Django
- Configuration optimisée pour la performance
- Support HTTPS (commenté, à activer en production)
- Support pour Let's Encrypt (commenté, à activer en production)

## Utilisation

### Développement

Pour le développement, vous pouvez continuer à utiliser le serveur Django directement :

```bash
docker-compose up
```

### Production

Pour la production, utilisez le fichier docker-compose.prod.yml qui inclut NGINX :

```bash
docker-compose -f docker-compose.prod.yml up -d
```

## Configuration HTTPS

Pour activer HTTPS en production :

1. Décommentez les sections HTTPS dans `conf.d/app.conf`
2. Remplacez `votre-domaine.com` par votre nom de domaine réel
3. Configurez Let's Encrypt pour obtenir des certificats SSL

## Personnalisation

Vous pouvez personnaliser la configuration en modifiant les fichiers suivants :

- `nginx.conf` : Configuration globale de NGINX
- `conf.d/app.conf` : Configuration spécifique à l'application