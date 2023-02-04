from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.index, name='ride'),
    path('<int:rid>/', views.getByRid, name='getByRid'),
    path('getu/<int:uid>/', views.getByUid, name='getByUid'),
    path('getd/<int:uid>/', views.getByDid, name='getByDid'),
    path('add/', views.addRide, name='addRide'),
    path('modify/',views.modifyRide,name='modifyRide'),
    path('searchd/<int:uid>/',views.SearchRideDriver,name='SearchRideDriver'),
    path('searchs/',views.SearchRideSharer,name='SearchRideSharer'),
]