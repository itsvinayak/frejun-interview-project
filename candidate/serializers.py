from rest_framework import serializers
from candidate.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"
