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
    profileImage = ResizedImageField(size=[200,200],quality=80, upload_to="profile/")
    uniqueId = models.UUIDField(primary_key = True,default =uuid4,editable = False)
    slug = models.SlugField(_("Slug"),max_length=500,unique=True,blank=True,null=True)

    date_created = models.DateTimeField(_("Created Date"), auto_now=False, auto_now_add=True)
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return '{} {} {}'.format(self.user.first_name,self.user.last_name,self.user.email)
    
    def save(self,*args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
        self.slug = slugify('{} {} {}'.format(self.user.first_name,self.user.last_name, self.user.email))
        self.last_updated = timezone.localtime(timezone.now())
        super(Profile, self).save(*args, **kwargs)



