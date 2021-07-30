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
    # Create a csv reader
    reader = csv.reader(open(file), delimiter=",")
    user = User.objects.get(id=user_id)
    # Iterate over the rows in the csv
    obj = []
    for row in reader:
        obj_data = Candidate(user=user, name=row[0], phone_number=row[1])
        obj.append(obj_data)
    with transaction.atomic():
        Candidate.objects.bulk_create(obj)
    print("done")
    return None
