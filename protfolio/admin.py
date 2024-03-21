from django.contrib import admin
from .models import Contact
from .models import Project, Glance, About, Cerficate
# Register your models here.
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(Glance)
admin.site.register(About)
admin.site.register(Cerficate)

