from django.urls import path, include
from django.contrib import admin
# from allauth.socialaccount.providers.google import urls as google_urls


from . import views


admin.site.site_header ="Login to Gautam singh"
admin.site.site_title="Wlcome to Gautam singh  Dashboard"
admin.site.index_title ="Wlcome to  this portle"
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('projects', views.project, name='project'),
    path('project_detail/<slug:course_slug>', views.project_detail, name='project_detail'),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('resume', views.resume, name="resume"),
    path('notes', views.notes, name="notes"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('social-auth/', include('social_django.urls')),
    # path('projects/', views.project_list, name='projects'),

]
