from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json
import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from apps.core.models import Repo_info

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class ProjectForm(forms.ModelForm):
        class Meta:
            model = Repo_info
            fields = [
                'project_name',
                'location',
                'github_link',
                'email',
                'description',
                 ]


def home(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request
        form = ProjectForm(request.POST)

        if form.is_valid():
            # Create a new repo object using the ModelForm's built-in .save()
            # giving it from the cleaned_data form.
            post = form.save()
            return redirect('/results/')
            

    else:
        # if a GET we'll create a blank form
        form = ProjectForm()
           
    context = {
        'form': form
    }

    return render(request, 'pages/home.html', context)

def results(request):

    repo = Repo_info.objects.all()

    project_list = []

    for link in repo:
        github_info = re.search(r'(?<=github\.com\/)((.*?)\/)(.*)', link.github_link)

        github_username = github_info.group(2)
        repo_name = github_info.group(3)

        stack_request_string = f'https://api.github.com/repos/{github_username}/{repo_name}/languages'
        
        stack_response = requests.get(stack_request_string)
        stack_json = stack_response.json()
        project_list.append({
            'link': link.github_link,
            'project_name': link.project_name,
            'description': link.description,
            'email':link.email,
            'labels': list(stack_json.keys()),
            'values': list(stack_json.values()),
        })

    context = {
        "repos": project_list,
    }

    return render(request, 'pages/projects.html', context)

def mission_statement(request):
    context = {
    }

    return render(request, 'pages/mission_statement.html', context)

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['dsmindich@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/contact/')
    return render(request, "pages/contact.html", {'form': form})

