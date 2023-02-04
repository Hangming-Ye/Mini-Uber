from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.index, name='home'),
    path('driver_page/', views.Dindex,name="Dindex"),
    path('<int:rid>/<str:role>', views.getByRid, name='getByRid'),
    path('getu/<int:uid>/', views.getByUid, name='getByUid'),
    path('getd/', views.getByDid, name='getByDid'),
    path('add/', views.addRide, name='addRide'),
    path('modify/',views.modifyRide,name='modifyRide'),
    path('searchd/',views.SearchRideDriver,name='SearchRideDriver'),
    path('searchs/',views.SearchRideSharer,name='SearchRideSharer'),
]