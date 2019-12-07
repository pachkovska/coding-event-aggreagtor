from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json
import re
from django.http import HttpResponse
from django.shortcuts import render
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

def home(request):
    #class EventForm(forms.ModelForm):
     #   class Meta:
      #      model = coding_event_query
       #     fields = ['text', 'image']

    context = {
    }

    return render(request, 'pages/home.html', context)

def results(request):

    repo = 'https://github.com/pachkovska/heroku-personal-app/branches/hello-there.git' #please note that this is a placeholder, this value will be coming from DB once it stored there after user submitted form

    github_info = re.search(r'(?<=github\.com\/)((.*?)\/)((.*?)\/)', repo)
    github_username = github_info.group(2)
    repo_name = github_info.group(4)

    stack_request_string = f'https://api.github.com/repos/{github_username}/{repo_name}/languages'
    
    stack_response = requests.get(stack_request_string)
    stack_json = stack_response.json()

    tech_stack = []
    
    code_total = sum(stack_json.values())

    for key, value in stack_json.items():
        tech_stack.append(f'{key}: {round(value/code_total*100, 1)}%')


    context = {
        "tech_stack": tech_stack,
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
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['dsmindich@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return render(request, "pages/contact.html", {'form': form})

