from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.index, name='home'),
    path('driver_page/', views.SearchRideDriver,name="SearchRideDriver"),
    path('<int:rid>/<str:role>', views.getByRid, name='getByRid'),
    path('getu/<int:uid>/', views.getByUid, name='getByUid'),
    path('add/', views.addRide, name='addRide'),
    path('modify/<int:rid>',views.modifyRide,name='modifyRide'),
    path('share/<int:rid>',views.addShare,name='addShare'),
    path('confirm/<int:rid>',views.confirmRide,name='confirmRide'),
    path('complete/<int:rid>',views.completeRide,name='completeRide'),
    path('searchd/',views.SearchRideDriver,name='SearchRideDriver'),
    path('searchs/',views.SearchRideSharer,name='SearchRideSharer'),
]