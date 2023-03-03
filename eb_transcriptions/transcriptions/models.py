from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from eb_transcriptions.custom_storages import PrivateMediaStorage

class Audiofile(models.Model):
    name = models.CharField(max_length=250, null=False, unique=True)
    file = models.FieldFile(upload_to="audio", storage=PrivateMediaStorage())
    format = models.CharField(max_length=20, null=False)

class Transcription(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="transcriptions", verbose_name="Bruger")
    title = models.CharField(max_length=250, null=False, unique=True, verbose_name="Titel")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oprettet")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Redigeret")
    text = models.TextField(verbose_name="Transkribering")
    audio_file = models.OneToOneField(Audiofile, on_delete=models.CASCADE)
