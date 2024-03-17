from django.shortcuts import render
from django.http import HttpResponse
from protfolio .models import Contact
from django.contrib import messages
from .models import Project, Glance
from django.utils.text import slugify

def home(request):
    # return HttpResponse("Hello, world. You're at the Gautam singh.")
    
    best_projects = Project.objects.filter(best_project=True)
    me_at_glance = Glance.objects.all()
    for glance in me_at_glance:
        temp_video_link = glance.video_link[32:]
        temp_video_link = "https://www.youtube.com/embed/"+temp_video_link
        glance.video_link = temp_video_link
    context = {'name':'gautam' ,
               'course':'djnago', 
               'projects': best_projects, 
               'me_at_glance': me_at_glance, 
            #    'video-link': temp_video_link
               }
    return render(request, 'home.html', context)


def about(request):
    # return HttpResponse("Hello, world. You're at the about.(/about)")
    return render(request, 'about.html')


def contact(request):
    if request.method== "POST":
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        desc= request.POST['content']
        # print(Name,email,phone,desc)
        contact= Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(
                request, "Your message has been successfully sent")
        # print("save all the date")

    # return HttpResponse("Hello, world. You're at the contact.(/contact)")
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




