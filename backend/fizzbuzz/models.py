from django.db import models

# Create your models here.
class Fizzbuzz(models.Model):
    # id = models.CharField(max_length=120, primary_key=True)
    # id = models.AutoField(primary_key=True)
    id = models.AutoField
    created_at = models.DateTimeField(auto_now_add=True)
    # useragent = models.CharField(max_length=120)
    message = models.CharField(max_length=120, blank=False)
    # message = models.TextField(blank=True, null=True)

    # @property
    # def get_fizzbuzz_id(self):
    #     return