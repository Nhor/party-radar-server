from rest_framework.decorators import \
    api_view, authentication_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .serializers import *
from .models import *


@api_view(['POST'])
@authentication_classes(()) # explicitly override to allow all
def login(request):
    """
    Login user using email and password as credentials.
    """
    credentials = LoginSerializer(data=request.POST)
    if not credentials.is_valid():
        return Response(credentials.errors,
            status=status.HTTP_400_BAD_REQUEST)
    email = credentials.data.get('email')
    password = credentials.data.get('password')
    user = User.objects.filter(email=email)
    if user:
        user = user.first()
        if user.check_password(password):
            Token.objects.get(user=user).delete()
            token = Token.objects.create(user=user)
            return Response({'status': 'ok', 'token': token.key})
    return Response({'status': 'Invalid credentials.'},
        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
def logout(request):
    """
    Logout already logged in user.
    """
    Token.objects.get(user=request.user).delete()
    return Response({'status': 'ok'})


@api_view(['POST'])
@authentication_classes(()) # explicitly override to allow all
def register(request):
    """
    Register new user with username, email and password.
    """
    credentials = RegisterSerializer(data=request.POST)
    if not credentials.is_valid():
        return Response(credentials.errors,
            status=status.HTTP_400_BAD_REQUEST)
    username = credentials.data.get('username')
    email = credentials.data.get('email')
    password = credentials.data.get('password')
    if User.objects.filter(username=username):
        return Response({'status': 'Username already in use.'},
            status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(email=email):
        return Response({'status': 'Email already in use.'},
            status=status.HTTP_400_BAD_REQUEST)
    if len(password) < 6:
        return Response({'status': 'Password too short.'},
            status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    token = Token.objects.create(user=user)
    return Response({'status': 'ok', 'token': token.key})
