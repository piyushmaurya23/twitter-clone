# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from twitter.locations.models import Location


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name'), blank=True, max_length=255)
    mobile_number = models.CharField(max_length=10, blank=True)
    about_me = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='users/profile/%m/', blank=True)
    location = models.ForeignKey(Location, blank=True, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


class UserAddress(models.Model):
    user = models.ForeignKey(User)
    address1 = models.CharField(max_length=120)
    address2 = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=30)
    pin_code = models.CharField(max_length=6)

    def get_absolute_url(self):
        return reverse("users:address_detail", kwargs={"pk": self.pk})
