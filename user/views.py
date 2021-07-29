from rest_framework.response import Response
from rest_framework.decorators import api_view

from user.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token


@api_view(["POST"])
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
        token = Token.objects.get(user=user).key
        data["token"] = token
    else:
        data = serializer.errors
    return Response(data)
