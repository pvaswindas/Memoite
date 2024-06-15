from rest_framework.serializers import ModelSerializer  # type: ignore
from .models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
