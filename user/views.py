from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from user.serializers import LoginSerializer, RegisterSerializer
from rest_framework.authtoken.models import Token


@api_view(["POST"])
@permission_classes((AllowAny,))
def registration_view(request):
    """
    Register a new user.
    """
    serializer = RegisterSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data["response"] = "successfully registered new user."
        data["email"] = user.email
        data["username"] = user.username
        token = Token.objects.get_or_create(user=user)[0].key
        data["token"] = str(token)
    else:
        data = serializer.errors
    return Response(data)


@api_view(["POST"])
@permission_classes((AllowAny,))
def login_view(request):
    """token based login api"""
    serializer = LoginSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = User.objects.get(email=serializer.data["username"])
        data["response"] = "successfully logged in."
        data["email"] = user.email
        data["username"] = user.username
        token = Token.objects.get_or_create(user=user)[0].key
        data["token"] = str(token)
    else:
        data = serializer.errors
    return Response(data)


@api_view(["POST"])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def logout(request):
    """ logout delete's token """
    try:
        request.user.auth_token.delete()
    except:
        pass
    return Response({"success": "Successfully logged out."}, status=status.HTTP_200_OK)
