from django.contrib import admin
from .models import Contact
from .models import Project, Glance
# Register your models here.
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(Glance)

