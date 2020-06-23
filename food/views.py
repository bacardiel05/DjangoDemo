# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader  # allows to load a template

# Create your views here.

# for every view there is a url, so views and urls go hand in hand


def index(request):
    item_list = Item.objects.all()

    context = {
        'item_list': item_list,  # pass item_list as item_list
    }
    return render(request, 'food/index.html', context)


def item(request):
    return HttpResponse('This is an item view')


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)
