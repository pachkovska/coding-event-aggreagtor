from django.shortcuts import render
#from models import coding_event_query

# Two example views. Change or delete as necessary.
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

    return render(request, 'pages/results.html', context)

def mission_statement(request):
    context = {
    }

    return render(request, 'pages/mission_statment.html', context)

def contact(request):
    context = {
    }

    return render(request, 'pages/contact.html', context)

