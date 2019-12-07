from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('results/', views.results, name='results'),
    path('mission_statement/', views.mission_statement, name='mission_statement'),
    path('contact/', views.contact, name='contact'),

]
