from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField

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
    collaborators = models.CharField(max_length=300, blank = True, null = True)
    description = RichTextField(config_name='default',max_length=300000,blank=True)
    technology = models.CharField(max_length=50)
    project_image = models.ImageField(upload_to='project_images/')
    demo_link = models.URLField(max_length=200)
    source_link = models.URLField(max_length=200)
    video_link = models.CharField(max_length=500, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    best_project = models.BooleanField(default=False)
    slug = models.CharField(max_length=1000, null=True,  blank=True)


    


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = slugify(self.title)
        super().save(*args, **kwargs)




class Glance(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    video_link = models.CharField(max_length = 500, blank=True, null=True)
    channel_link = models.CharField(max_length = 500)


class Cerficate(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='media/certificates')
    news = models.TextField()
    bugFix = models.TextField()

class About(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    dob = models.CharField(max_length=20)
    image = models.ImageField(upload_to='protfolio/static/footer_profile')
    video_link = models.CharField(max_length=400)
