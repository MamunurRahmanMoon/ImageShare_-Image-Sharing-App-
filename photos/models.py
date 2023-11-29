from django.db import models
from django.contrib.auth.models import User as Baseuser

# Create your models here.

class Photo(models.Model):
    user = models.ForeignKey(Baseuser, on_delete=models.CASCADE, default=1)  ## Django Base User

    file = models.FileField(upload_to='files')
    url = models.URLField()
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-timestamp"]



