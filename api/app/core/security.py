from fastapi import HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.config import settings

_bearer = HTTPBearer(auto_error=False)


def verify_token(credentials: HTTPAuthorizationCredentials = Security(_bearer)) -> None:
    """Valida Bearer token nos endpoints de entrada (sensor e webhook).
    Se WEBHOOK_SECRET não estiver configurado, aceita qualquer requisição (modo dev).
    """
    secret = settings.webhook_secret
    if not secret:
        return

    if not credentials or credentials.credentials != secret:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou ausente.",
            headers={"WWW-Authenticate": "Bearer"},
        )
