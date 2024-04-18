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
    technology = models.CharField(max_length=50)
    project_image = models.ImageField(upload_to='project_images/')
    source_link = models.URLField(max_length=200)
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


class NodeProject(models.Model):
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE, related_name="node_project")
    heading = models.CharField(max_length = 500, null=True, blank=True)
    description = RichTextField(config_name='default',max_length=300000,blank=True)
    demo_link = models.URLField(max_length=200)
    video_link = models.CharField(max_length=500, blank=True, null=True)
    slug = models.CharField(max_length=1000, null=True,  blank=True)

    def __str__(self):
        return self.heading
    
    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = slugify(self.heading)
        super().save(*args, **kwargs)


class Glance(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    video_link = models.CharField(max_length = 500, blank=True, null=True)
    channel_link = models.CharField(max_length = 500)


class Cerficate(models.Model):
    description = models.TextField()
    image1 = models.ImageField(upload_to='media/certificates/', null=True)
    image2 = models.ImageField(upload_to='media/certificates/', null=True)
    image3 = models.ImageField(upload_to='media/certificates/', null=True)
    news = models.TextField()
    bugFix = models.TextField()

class About(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    dob = models.CharField(max_length=20)
    image = models.ImageField(upload_to='footer_profile/', null=True)
    
    video_link = models.CharField(max_length=400)

# models for resume
class Resume(models.Model):
    image = models.ImageField(upload_to="resume")
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    twitter = models.CharField(max_length=300, null=True)
    leetcode = models.CharField(max_length=300, null= True)
    github = models.CharField(max_length=300, null= True)
    linkedIn = models.CharField(max_length=300, null= True)

class Education(models.Model):
    university = models.CharField(max_length=400)
    branch = models.CharField(max_length=300)
    marks = models.CharField(max_length=10)
    date = models.CharField(max_length=30)
    description = models.TextField()

class Skill(models.Model):
    language = models.CharField(max_length=200, null=True)
    developement = models.CharField(max_length=200, null=True)
    mobile_developement = models.CharField(max_length=400, null=True)
    testing = models.CharField(max_length=400, null=True)
    designing = models.CharField(max_length=400, null=True)
    tools = models.CharField(max_length=400, null=True)
    video_editing = models.CharField(max_length=400, null=True)


class Experience(models.Model):
    title = models.CharField(max_length=400)
    subtitle = models.CharField(max_length=400)
    description = models.TextField()
    date = models.CharField(max_length=400)
    company = models.CharField(max_length=400)
    location = models.CharField(max_length=400)

# resume projects
class AcademicProject(models.Model):
    title = models.CharField(max_length=400, null=True)
    desct = models.CharField(max_length=400, null=True)
    key_skills = models.CharField(max_length=400, null=True)
    repository = models.CharField(max_length=400, null=True)
    date = models.CharField(max_length=400, null=True)
    author = models.CharField(max_length=400, null=True)


class Achievement(models.Model):
    title = models.CharField(max_length=400, null=True)
    description = models.TextField()
    date  = models.CharField(max_length=400, null=True)
    specialization = models.CharField(max_length=400, null=True)

class Certificate(models.Model):
    title = models.CharField(max_length=300, null=True)
    description = models.TextField()
    link = models.CharField(max_length=300, null=True)
    issue_date = models.CharField(max_length=300, null=True)


class Interest(models.Model):
    name = models.CharField(max_length=100)

class Language(models.Model):
    name = models.CharField(max_length=300)

class Note(models.Model):
    image = models.ImageField(upload_to="notes")
    title = models.CharField(max_length=300, null=True)
    content = models.TextField()
    pdf = models.FileField(upload_to="notes_pdf")






    



    




