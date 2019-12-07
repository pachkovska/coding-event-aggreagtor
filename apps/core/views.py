from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
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
    context = {
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

