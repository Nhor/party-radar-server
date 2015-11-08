from rest_framework.decorators import \
    api_view, authentication_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import *
from .models import *


@api_view(['POST'])
@authentication_classes(()) # explicitly override to allow all
def login_api(request):
    """
    Login user using email and password as credentials.
    """
    credentials = LoginSerializer(data=request.POST)
    if not credentials.is_valid():
        return Response(credentials.errors,
            status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.get(email=credentials.data.get('email'))
    if user:
        Token.objects.get(user=user).delete()
        token = Token.objects.create(user=user)
        return Response({'status': 'ok', 'token': token.key})
    return Response({'status': 'invalid'},
        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_api(request):
    """
    Logout already logged in user.
    """
    Token.objects.get(user=request.user).delete()
    return Response({'status': 'ok'})
