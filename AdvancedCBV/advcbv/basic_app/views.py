from django.shortcuts import render
from . import models
from django.views.generic import (View, TemplateView,
                                ListView, DetailView)


class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Hello i am injected'
        return context

class SchoolListView(ListView):
    #context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'
