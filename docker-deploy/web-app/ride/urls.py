from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='ride'),
    path('getr/<int:rid>', views.getByRid, name='getByRid'),
    path('getu/<int:uid>', views.getByUid, name='getByUid'),
    path('add', views.addRide, name='addRide'),
    path('modify',views.modifyRide,name='modifyRide'),
    path('searchd',views.SearchRideDriver,name='SearchRideDriver'),
    path('searchs',views.SearchRideSharer,name='SearchRideSharer'),
]