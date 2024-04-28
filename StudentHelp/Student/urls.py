from django.urls import path
from . import views
from .views import StageCreateView, LogementCreateView, EvenementCreateView, TransportCreateView


urlpatterns = [
    # URLs for posts
    path('', views.acceuil, name='acceuil'),
    path('inscription/',views.inscription, name = 'inscription'), 
    path('change-password/',views.change_password, name='change_password'),
    

    path('create-stage/', StageCreateView.as_view(), name='create-stage'),
    path('create-logement/', LogementCreateView.as_view(), name='create-logement'),
    path('create-evenement/', EvenementCreateView.as_view(), name='create-evenement'),
    path('create-transport/', TransportCreateView.as_view(), name='create-transport'),

    
    path('logement/', views.LogementList, name='logement-list'),
    path('event/', views.EventList, name='event-list'),
    path('stage/', views.StageList, name='stage-list'),
    path('transport/', views.TransportList, name='transport-list'),

]
