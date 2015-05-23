# -*- coding: utf-8 -*-
from models import Journal_technicks, Journal_workers, Journal_sdacha
from django.views.generic.base import TemplateView
from django.db import models

sdacha = Journal_sdacha.objects.all()
tec = Journal_technicks.objects.all()
work = Journal_workers.objects.all()



class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
       # sdacha = Journal_sdacha
        #tec = Journal_technicks
        #work = Journal_workers
        context.update(
            {
                'sdacha': sdacha,
                'tec':tec,
                'work':work,
            }
        )
        return context
