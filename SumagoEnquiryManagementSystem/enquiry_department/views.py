from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,UpdateView
from enquiry_department.models import *
from django.urls import reverse_lazy

# Create your views here.

#Home Page
class Index(TemplateView):
    template_name = 'enquiry_department/index.html'

#Courses
class AddCourses(CreateView):
    model = Course
    fields = "__all__"
    success_url = reverse_lazy('enquiry_department:index')

    def get_form(self, form_class=None):
        form = super(AddCourses, self).get_form(form_class)
        for visible in form.visible_fields():
            visible.field.widget.attrs.update({'class' : 'form-control'})
        return form
        
class CoursesList(ListView):
    model = Course

class UpdateCourses(UpdateView):
    model = Course
    fields = "__all__"
    success_url = reverse_lazy('enquiry_department:courses_list')
    def get_form(self, form_class=None):
        form = super(UpdateCourses, self).get_form(form_class)
        for visible in form.visible_fields():
            visible.field.widget.attrs.update({'class' : 'form-control'})
        return form
    
#Enquirys
class EnquiryList(ListView):
    model = Enquiry

class AddEnquiry(CreateView):
    model = Enquiry
    fields = '__all__'
    success_url = reverse_lazy('enquirys_list')
