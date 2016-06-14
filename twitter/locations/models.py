from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=10)
    parent_id = models.IntegerField()
    location_type = models.CharField(max_length=15)
    longitude = models.CharField(max_length=30, blank=True, null=True)
    lattitude = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return "%d-%s" % (self.id, self.name)


