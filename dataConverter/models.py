from django.db import models

# Create your models here.

class AbstracFileUploader(models.Model):
    abstract = True
    file = models.FileField(upload_to='uploads/')


class CreateCBSStructure(AbstracFileUploader):
    pass

class CreateEstimate(AbstracFileUploader):
    pass

