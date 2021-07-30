import csv

from celery import shared_task
from django.contrib.auth.models import User
from django.db import transaction

from candidate.models import Candidate


@shared_task
def uploadFile(file, user_id):
    """
    Uploads a file to the server.
    """
    file = list(file.split('\n'))
    user = User.objects.get(id=user_id)
    # Iterate over the rows in the csv
    obj = []
    for row in file:
        temp = row.split(',')
        print(temp)
        obj_data = Candidate(user=user, name=temp[0], phone_number=temp[1])
        obj.append(obj_data)
    with transaction.atomic():
        Candidate.objects.bulk_create(obj)
    print("done")
    return None
