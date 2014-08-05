from __future__ import unicode_literals, absolute_import

from django.contrib.admin import site, ModelAdmin

from . import models

site.register(models.Wossname, ModelAdmin)
