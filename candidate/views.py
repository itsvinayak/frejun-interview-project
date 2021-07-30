from django.conf import settings
import os

from django.contrib.auth.models import User
from candidate.models import Candidate
from candidate.serializers import CandidateSerializer
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .tasks import uploadFile
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token


@api_view(["put"])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def upload_file(request):
    file_obj = request.FILES["file"]
    if file_obj.name.split(".")[-1] != "csv":
        return Response({"message": "File type is not allowed"}, status=400)
    ## reading file 
    file = str(file_obj.read())
    uploadFile.delay(file=file , user_id=request.user.id)

    print(file_obj.read())
    return Response({"file": "uploaded"}, status=201)


@api_view(
    [
        "GET",
    ]
)
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def get_candidate(request):
    """ get candidates with pagination of 10 """
    paginator = PageNumberPagination()
    paginator.page_size = 10
    user_id = Token.objects.get(key=request.auth.key).user_id
    user = User.objects.get(id=user_id)
    candidate_objects = Candidate.objects.filter(user=user)
    result_page = paginator.paginate_queryset(candidate_objects, request)
    serializer = CandidateSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
