
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView
from enquiry_department.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


    

class Index(LoginRequiredMixin,UserPassesTestMixin,TemplateView):
    template_name = 'enquiry_department/index.html'
    def test_func(self):
        return self.request.user.groups.filter(name='enquiry').exists()

    
#Courses
class AddCourses(UserPassesTestMixin,CreateView):
    model = Course
    fields = "__all__"
    success_url = reverse_lazy('enquiry_department:index')

    def get_form(self, form_class=None):
        form = super(AddCourses, self).get_form(form_class)
        for visible in form.visible_fields():
            visible.field.widget.attrs.update({'class' : 'form-control'})
        return form
    
    def test_func(self):
        return self.request.user.groups.filter(name='enquiry').exists()

        
class CoursesList(UserPassesTestMixin,ListView):
    model = Course
    def test_func(self):
        return self.request.user.groups.filter(name='enquiry').exists()


class UpdateCourses(UpdateView):
    model = Course
    fields = "__all__"
    success_url = reverse_lazy('enquiry_department:courses_list')
    def get_form(self, form_class=None):
        form = super(UpdateCourses, self).get_form(form_class)
        for visible in form.visible_fields():
            visible.field.widget.attrs.update({'class' : 'form-control'})
        return form
    def test_func(self):
        return self.request.user.groups.filter(name='enquiry').exists()


#Enquirys
class EnquiryList(UserPassesTestMixin,ListView):
    model = Enquiry
    def test_func(self):
        return self.request.user.groups.filter(name='enquiry').exists()

class AddEnquiry(CreateView):
    model = Enquiry
    fields = '__all__'
    success_url = reverse_lazy('enquirys_list')
