# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField( null = True, blank = True)
    location = models.CharField(max_length=120, default='mylocation', blank = True, null = True)
    Jobs = models.CharField(max_length=120, null=True, blank = True)

    def __unicode__(self):
        return self.name
