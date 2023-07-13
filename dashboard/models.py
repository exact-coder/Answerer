from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from uuid import uuid4
from django_resized import ResizedImageField

import os


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    position_title = models.CharField(_("Position Title"), max_length=50)
    call = models.IntegerField(_("Call"),max_length=16)
    address = models.CharField(_("Address"), max_length=200)
    description = models.TextField(_("Descrive Yourself's"))
    

