# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import profile


class profileAdmin(admin.ModelAdmin):
    class meta:
        model = profile
admin.site.register(profile,profileAdmin)


# Register your models here.
