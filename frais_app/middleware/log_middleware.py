import logging

logger = logging.getLogger('django.request')  # On cible le logger qu’on a défini dans settings

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  # Django passe la fonction pour exécuter la requête

    def __call__(self, request):
        # On exécute la vue et récupère la réponse
        response = self.get_response(request)

        # On récupère l’utilisateur s’il est connecté, sinon "Anonymous"
        user = request.user if request.user.is_authenticated else 'Anonymous'

        # On récupère l’adresse IP du client
        ip = request.META.get('REMOTE_ADDR', '')

        # On écrit un message de log avec toutes les infos utiles
        logger.info(
            f"{request.method} {request.path} {response.status_code}",
            extra={'client_ip': ip, 'user': str(user)}  # On passe nos infos personnalisées au format
        )

        return response  # On renvoie la réponse normalement
