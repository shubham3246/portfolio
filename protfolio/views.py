from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


# Importing models
from protfolio.models import Contact, Project, Glance, About, Cerficate, Resume, Note
from django.contrib import messages
from django.utils.text import slugify
from proname import settings
import re

import os
from dotenv import load_dotenv

load_dotenv()

# Regular expression pattern to clean HTML tags
CLEANR = re.compile('<.*?>') 

# Function to clean HTML tags from a string
def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext

# Home page view
def home(request):
    # Fetching best projects, me at glance info, and certificates
    best_projects = Project.objects.filter(best_project=True)
    me_at_glance = Glance.objects.all()
    certificate = Cerficate.objects.all()
    
    # Modifying video links for me at glance info
    for glance in me_at_glance:
        temp_video_link = glance.video_link[32:]
        temp_video_link = "https://www.youtube.com/embed/"+temp_video_link
        glance.video_link = temp_video_link

    # Fetching about info
    about = About.objects.all()
    
    # Constructing context dictionary
    context = {
        'name': 'gautam',
        'course': 'djnago',
        'projects': [
            {
                "title": project.title,
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
        'about': about[0]
    }
    return render(request, 'portfolio/home.html', context)


# About page view
def about(request):
    return render(request, 'portfolio/about.html')


def resume(request):
    data = Resume.objects.all()
    context = {
        'image': f'{settings.MEDIA_URL}{data[0].image}',
        'email': data[0].email,
        'phone': data[0].phone,
        'address': data[0].address
    }
    return render(request, 'portfolio/resume.html', context=context)


# Contact page view
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['content']
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, "Your message has been successfully sent")

    return render(request, 'portfolio/contact.html')


# Projects page view
def project(request):
    projects = Project.objects.all()
    context = {
        'projects': [
            {
                "title": project.title,
                "technology": project.technology,
                "image": project.project_image,
                "created_date": project.created_date,
                "slug": project.slug
            }
            for project in projects
        ]
    }
    return render(request, 'portfolio/project.html', context)


# Project detail page view
def project_detail(request, course_slug):
    try:
        curr_proj = request.GET.get('proj')
        project = Project.objects.get(slug=course_slug)
        required_views = project.node_project.all()

        curr_desc = None
        curr_video = None

        if curr_proj is not None and curr_proj != "":
            curr = project.node_project.get(slug=curr_proj)
            curr_desc = curr.description
            temp_video_link = curr.video_link
            if temp_video_link is not None and temp_video_link != "":
                temp_video_link = temp_video_link[32:]
                temp_video_link = "https://www.youtube.com/embed/" + temp_video_link
                modified_url_string = re.sub(r'&.*$', '', temp_video_link)
                curr_video = modified_url_string
            else:
                curr_video = None

        else:
            curr = required_views[0]
            curr_desc = curr.description
            temp_video_link = curr.video_link
            if temp_video_link is not None and temp_video_link != "":
                temp_video_link = required_views[0].video_link[32:]
                temp_video_link = "https://www.youtube.com/embed/" + temp_video_link
                modified_url_string = re.sub(r'&.*$', '', temp_video_link)
                curr_video = modified_url_string
            else:
                curr_video = None

        next_link = None
        prev_link = None

        for link in range(len(required_views)):
            if required_views[link] == curr:
                if link < len(required_views) - 1:
                    next_link = f"?proj={required_views[link+1].slug}"
                if link > 0:
                    prev_link = f"?proj={required_views[link-1].slug}"

        context = {
            "title": project.title,
            "description": curr_desc,
            "technology": project.technology,
            "collaborators": project.collaborators,
            "image": project.project_image,
            "source_link": project.source_link,
            "video": curr_video,
            "all_projects": required_views,
            "slug": project.slug,
            "next_link": next_link,
            "prev_link": prev_link
        }

        return render(request, "portfolio/project_detail.html", context=context)
    
    except Exception as e:
        return HttpResponse("Add a node to the project")

def notes(request):
    notes = Note.objects.all()
    context = {
        "notes" : [
            {
                "image": f'{settings.MEDIA_URL}{note.image}',
                "title": note.title,
                "content": note.content,
                "pdf": f'{settings.MEDIA_URL}{note.pdf}'
            }
            for note in notes
        ]
    }
    return render(request, "portfolio/notes.html", context=context)

# Search functionality view
def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allPosts = Project.objects.none()
    else:
        allPostsTitle = Project.objects.filter(title__icontains=query)
        allPostsTechnology = Project.objects.filter(technology__icontains=query)
        allPostsCollaborators = Project.objects.filter(collaborators__icontains=query)
        allPosts = allPostsTitle.union(allPostsCollaborators, allPostsTechnology)
    if allPosts.count() == 0:
        messages.warning(request, "No search results found. Please refine your query.")
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'portfolio/search.html', params)


# User sign up view
def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Input validation
        if len(username) < 10:
            messages.error(request, " Your username must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, " Passwords do not match")
            return redirect('home')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your iCoder has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


# User login view
def handeLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")


# User logout view
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

# ---------------------------------------

