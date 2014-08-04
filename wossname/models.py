from __future__ import absolute_import, unicode_literals

from django.db import models

class Wossname(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.name)
