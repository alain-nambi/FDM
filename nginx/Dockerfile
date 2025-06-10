FROM nginx:1.25-alpine

# Supprimer la configuration par défaut
RUN rm /etc/nginx/conf.d/default.conf

# Copier les fichiers de configuration
COPY nginx.conf /etc/nginx/nginx.conf
COPY conf.d/ /etc/nginx/conf.d/

# Créer les répertoires nécessaires pour Let's Encrypt (pour une utilisation future)
RUN mkdir -p /var/www/certbot

# Exposer les ports
EXPOSE 80 443

# Commande par défaut pour démarrer NGINX
CMD ["nginx", "-g", "daemon off;"]