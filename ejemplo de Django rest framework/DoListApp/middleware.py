import jwt
from django.http import JsonResponse
from django.conf import settings

def auth_required(get_response):
    def middleware(request):
        auth = request.headers.get("Authorization", None)
        if not auth:
            return JsonResponse({"error": "Token requerido"}, status=401)

        try:
            token = auth.split()[1]
            payload = jwt.decode(
                token,
                settings.PUBLIC_KEY,
                algorithms=settings.ALGORITHMS,
                audience=settings.API_IDENTIFIER,
                issuer=settings.JWT_ISSUER
            )
            request.user = payload  # Guarda la info del usuario en la request
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token expirado"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Token inválido"}, status=401)

        return get_response(request)

    return middleware
