from django.db import models

# Create your models here.

class Logs(models.Model):
    local_id=models.BigIntegerField()
    device_address=models.CharField(max_length=50)
    c02=models.FloatField()
    tv02=models.FloatField()
    pm25=models.FloatField()
    pm10=models.FloatField()
    read_at=models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True)

# def __str__(self):
#     return self.read_at

