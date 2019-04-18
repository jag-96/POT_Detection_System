from django.db import models


class List_data_point(models.Model):
    longitude = models.FloatField(name='longitude',max_length=9)
    latitude = models.FloatField(name='latitude',max_length=9)
    priority = models.IntegerField(default=0)
    def retrieve_point(self):
        return self.longitude, self.latitude, self.priority
        