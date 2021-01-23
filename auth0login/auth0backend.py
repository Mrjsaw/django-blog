from urllib import request
from jose import jwt
from social_core.backends.oauth import BaseOAuth2

class Auth0(BaseOAuth2):
    """Auth0 OAuth authentication backend"""
    name = "auth0"
    SCOPE_SEPARATOR = " "
    ACCESS_TOKEN_METHOD = "POST"
    REDIRECT_STATE = False
    EXTRA_DATA = [("picture", "picture"), ("email", "email")]
    def authorization_url(self):
        return "https://cyberbl0g.herokuapp.com/authorize"
    def access_token_url(self):
        return "https://cyberbl0g.herokuapp.com/oauth/token"
    def get_user_id(self, details, response):
        """Return current user id."""
        return details["user_id"]
    def get_user_details(self, response):
        # Obtain JWT and the keys to validate the signature
        id_token = response.get("id_token")
        jwks = request.urlopen(
            "https://cyberbl0g.herokuapp.com/.well-known/jwks.json"
        )
        issuer = "https://cyberbl0g.herokuapp.com/"
        audience = self.setting("KEY")  # CLIENT_ID
        payload = jwt.decode(
            id_token,
            jwks.read(),
            algorithms=["RS256"],
            audience=audience,
            issuer=issuer,
        )
        return {
            "username": payload["nickname"],
            "first_name": payload["name"],
            "picture": payload["picture"],
            "user_id": payload["sub"],
            "email": payload["email"],
        }