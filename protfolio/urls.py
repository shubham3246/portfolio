from django.urls import path
from django.contrib import admin

from . import views


admin.site.site_header ="Login to Gautam singh"
admin.site.site_title="Wlcome to Gautam singh  Dashboard"
admin.site.index_title ="Wlcome to  this portle"
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('projects', views.project, name='project'),
    path('project_detail/<slug:course_slug>', views.project_detail, name='project_detail'),
    # path('projects/', views.project_list, name='projects'),

]
