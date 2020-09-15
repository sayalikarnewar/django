from django.db import models
from datetime import datetime

# Create your models here.
class Tutorial(models.Model):
    Tutorial_title = models.CharField(max_length = 200)
    Tutorial_content = models.TextField()
    Tutorial_published = models.DateTimeField("date published", default =datetime.now())

    def __str__(self):
        return self.Tutorial_title 