from django.shortcuts import render
from django.http import HttpResponse
from protfolio .models import Contact
from django.contrib import messages
from .models import Project, Glance, About, Cerficate
from django.utils.text import slugify
import re
# as per recommendation from @freylis, compile once only
CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

def home(request):
    best_projects = Project.objects.filter(best_project=True)
    me_at_glance = Glance.objects.all()
    certificate = Cerficate.objects.all()
    for glance in me_at_glance:
        temp_video_link = glance.video_link[32:]
        temp_video_link = "https://www.youtube.com/embed/"+temp_video_link
        glance.video_link = temp_video_link


    about = About.objects.all()
    # about[0].image = "img/footer_card_profile.jpg"
    # print(about[0].image)
    
    context = {
        'name':'gautam' ,
            'course':'djnago', 
            'projects': [
                {
                    "title": project.title,
                    "description": cleanhtml(project.description),
                    "technology": project.technology,
                    "image": project.project_image,
                    "created_date": project.created_date,
                    "slug": project.slug
                }
                for project in best_projects
            ], 
            'me_at_glance': me_at_glance, 
            'certificate1': certificate[0].image1,
            'certificate2': certificate[0].image2,
            'certificate3': certificate[0].image3,
            'about' : about[0]
        }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method== "POST":
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        desc= request.POST['content']
        contact= Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(
                request, "Your message has been successfully sent")

    return render(request, 'contact.html')



def project(request ):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'project.html', context)

def project_detail(request, course_slug):
    project = Project.objects.get(slug=course_slug)

    temp_video_link = project.video_link[32:]
    temp_video_link = "https://www.youtube.com/embed/"+temp_video_link

    context = {
        "title": project.title,
        "description": project.description,
        "technology": project.technology,
        "collaborators": project.collaborators,
        "image": project.project_image,
        "demo_link": project.demo_link,
        "source_link": project.source_link,
        "video_link": temp_video_link
    }

    print(temp_video_link)
    return render(request, "project_detail.html", context=context)


# def project(request):
#     projects = Project.objects.all()
#     for project in projects:
#         project.slug = slugify(project.title) # Add the slug field to each Project instance
#     context = {'projects': projects}
#     return render(request, 'project.html', context)




