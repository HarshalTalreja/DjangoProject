from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView,
                                ListView, DetailView,
                                CreateView, DeleteView, UpdateView)


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

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('schoollist')

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class StudentListView(ListView):
    #context_object_name = 'schools'
    model = models.Student

class StudentDetailView(DetailView):
    context_object_name = 'student_detail'
    model = models.Student
    template_name = 'basic_app/student_detail.html'
    
