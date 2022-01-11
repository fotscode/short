from django.db import models

# Create your models here.
class URL(models.Model):
    def __str__(self):
        return self.url_short

    url_text = models.CharField(max_length=390)
    url_short = models.CharField(max_length=10, unique=True, null=False, blank=False)
    pub_date = models.DateTimeField("date published")
