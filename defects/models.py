from django.db import models
from pytz import timezone

# Create your models here.
class Defect(models.Model):
    defectid = models.CharField(max_length=200)
    defect_name = models.CharField(max_length=200)
    assignedby = models.CharField(max_length=200)
    assignedto = models.CharField(max_length=200)
    description = models.TextField()
    defect_edit = models.CharField(max_length=100) # added to edit the form
    defect_status = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)


class defect_screen_short(models.Model):
    defect_name = models.ForeignKey(Defect, on_delete=models.CASCADE)
    defect_img = models.ImageField(upload_to='defects/', null=True, blank=True)