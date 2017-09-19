# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.core import serializers
from django.views.generic import ListView

from liveupdate.models import Update
from django.shortcuts import render

object_list = Update.objects.all()


class ObjectList(ListView):
    model = Update
    template_name = 'liveupdate/update_list.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        item_list = super(ObjectList, self).get_context_data(**kwargs)
        return item_list


def update_after(request, id):
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(serializers.serialize("json",
                                         Update.objects.filter(pk__gt=id)))
    return response
