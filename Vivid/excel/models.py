from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model

class Table(models.Model):
    licno = models.IntegerField()
    ild = models.DateField()
    fno = models.CharField(max_length = 250)
    iec = models.IntegerField()
    pname = models.CharField(max_length = 300)
    lic = models.CharField(max_length = 300)
    fob = models.FloatField()
    cif = models.FloatField()

@property
def lifespan(self):
    return '%s - present' % self.ild.strftime('%m/%d/%Y')
