#!/bin/sh

echo "📡 Attente de la base de données..."

# On vérifie que le service db est prêt
until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  echo "⏳ En attente de PostgreSQL à $POSTGRES_HOST:$POSTGRES_PORT..."
  sleep 1
done

echo "✅  PostgreSQL est prêt !"

echo "⚙️  Création des logs..."
mkdir -p /app/logs
touch logs/django.log
chmod 664 logs/django.log
echo "✅  Tous les services sont prêts!"

echo "📦  Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

echo "⚙️  Exécution des migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput


# Exécute la commande CMD
exec "$@"