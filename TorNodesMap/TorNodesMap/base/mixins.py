from django.contrib.gis.db import models
from django.utils import timezone


class BaseMixin(models.Model):
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """

        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(BaseMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True
