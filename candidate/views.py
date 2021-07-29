from django.conf import settings
import os
from config.celery import app
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .tasks import uploadFile


@api_view(["put"])
@permission_classes((IsAuthenticated,))
def upload_file(request):
    file_obj = request.FILES["file"]
    if file_obj.name.split(".")[-1] != "csv":
        return Response({"message": "File type is not allowed"}, status=400)
    file_path = os.path.join(settings.MEDIA_ROOT + "uploads/", file_obj.name)
    with open(file_path, "wb+") as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)
    print(request.user.id)
    uploadFile.delay(file=file_path, user_id=request.user.id)
    print(file_path, "-->>", file_obj.name)
    return Response({"file": "uploaded"}, status=201)
