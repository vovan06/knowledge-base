from django.db import models

# Create your models here.

class Catalog(models.Model):
    title = models.CharField(max_length=20,)


class Document(models.Model):
    title = models.CharField(max_length=30,)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    private_access = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    catalog = models.ForeignKey(Catalog, default=None, blank=True, on_delete=models.CASCADE)