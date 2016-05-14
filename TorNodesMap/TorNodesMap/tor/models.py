from __future__ import unicode_literals

from TorNodesMap.base.mixins import BaseMixin
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class Node(BaseMixin):
    ip = models.GenericIPAddressField(db_index=True)
    latitude = models.FloatField(verbose_name='Latitude')
    longitude = models.FloatField(verbose_name='Longitude')
    location = models.PointField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.location = Point(self.latitude, self.longitude)
        super(Node, self).save(*args, **kwargs)
