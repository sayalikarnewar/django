from django.db import models
from datetime import datetime
# Create your models here.


class TutorialCategory(models.Model):

    Tutorial_category = models.CharField(max_length=200, default=1)
    Category_summary = models.CharField(max_length=200, default=1)

    class meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.Tutorial_category


class TutorialSeries(models.Model):
    Tutorial_series = models.CharField(max_length=200, default=1)

    Tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.CASCADE)
    Series_summary = models.CharField(max_length=200, default=1)

    class meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.Tutorial_series



class Tutorial(models.Model):
    Tutorial_title = models.CharField(max_length = 200)
    Tutorial_content = models.TextField()
    Tutorial_published = models.DateTimeField("date published", default =datetime.now())

    Tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.CASCADE)


    def __str__(self):
        return self.Tutorial_title 