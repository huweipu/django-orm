from django.db import models

# Create your models here.
class Bock(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.title