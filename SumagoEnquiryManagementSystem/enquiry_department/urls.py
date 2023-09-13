from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from enquiry_department.views import *

app_name = 'enquiry_department'

urlpatterns = [
    path('',Index.as_view(),name="index"),
    #Courses
    path('courses_list/',CoursesList.as_view(),name='courses_list'),
    path('add_courses/',AddCourses.as_view(),name='add_courses'),
    path('update_courses/<int:pk>/',UpdateCourses.as_view(),name='update_courses'),

    #Enquiry
    path('enquirys_list/',EnquiryList.as_view(),name='enquirys_list')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
