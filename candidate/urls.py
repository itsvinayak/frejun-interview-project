from django.urls import path
from candidate.views import upload_file, get_candidate

urlpatterns = [
    path("upload/", upload_file, name="upload_file"),
    path("show/", get_candidate, name="show"),
]
