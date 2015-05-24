# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from models import Journal_technicks, Journal_workers, Journal_sdacha
from django.views.generic.base import TemplateView, View
from django.db import models


class Journal_technicksView(View):
    template_name = "index.html0"

    def post (self, *args, **kwargs):
        typ_value = self.request.POST['typ']
        model_value = self.request.POST['model']
        price_value = self.request.POST['price']
        condition_value = self.request.POST['condition']
        availability_value = self.request.POST['availability']
        Journal_technicks.objects.create(typ=typ_value, model=model_value, price=price_value,
                                         condition=condition_value, availability=availability_value)
        return redirect('/')


class DeleteJournal_technicks(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        tec_delete = self.request.POST['delete_tec']
        Journal_technicks.objects.filter(id=int(tec_delete)).delete()
        return redirect('/')


class Journal_workersView(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        surname_value = self.request.POST['surname']
        name_value = self.request.POST['name']
        fname_value = self.request.POST['fname']
        office_value = self.request.POST['office']
        Journal_workers.objects.create(surname=surname_value, name=name_value, fname=fname_value, office=office_value)
        return redirect('/')


class DeleteJournal_workers(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        work_delete = self.request.POST['delete_work']
        Journal_workers.objects.filter(id=int(work_delete)).delete()
        return redirect('/')

class Journal_sdachaView(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        summa_value = self.request.POST['summa']
        ID_tec_value = self.request.POST['ID_tec']
        fio_value = self.request.POST['fio']
        vzitie_value = self.request.POST['vzitie']
        vozvr_value = self.request.POST['vozvr']
        cdacha_value = self.request.POST['cdacha']
        opozd_value = self.request.POST['opozd']
        document_value = self.request.POST['document']
        Journal_sdacha.objects.create(summa=summa_value, ID_tec=ID_tec_value, fio=fio_value, vzitie=vzitie_value,
                                      vozvr=vozvr_value, cdacha=cdacha_value, opozd=opozd_value, document=document_value)
        return redirect('/')

class DeleteJournal_sdacha(View):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        sdacha_delete = self.request.POST['delete_sdacha']
        Journal_sdacha.objects.filter(id=int(sdacha_delete)).delete()
        return redirect('/')


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        sdacha = Journal_sdacha.objects.all()
        tec = Journal_technicks.objects.all()
        work = Journal_workers.objects.all()
        context.update(
            {
                'sdacha': sdacha,
                'tec':tec,
                'work':work,
            }
        )
        return context
