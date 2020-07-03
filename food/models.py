# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Item(models.Model):
    # aids in getting item name
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=600, default="https://cdn.dribbble.com/users/1012566/screenshots/4187820/topic-2.jpg")
    #https://media.gettyimages.com/photos/sliced-pizza-on-chopping-board-overhead-view-picture-id763156339?s=2048x2048