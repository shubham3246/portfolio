from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class Contact(models.Model):

    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    desc = models.TextField()
    timeStamp = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return 'massage from' + self.name + '-' + self.email
    

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    project_image = models.ImageField(upload_to='project_images/')
    demo_link = models.URLField(max_length=200)
    source_link = models.URLField(max_length=200)
    video_link = models.CharField(max_length=500, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    slug = models.CharField(max_length=1000, null=True,  blank=True)
    


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = slugify(self.title)
        super().save(*args, **kwargs)
