from django.urls import path
from . import views

urlpatterns = [
    # example:
    path('user_reg', views.user_reg),
    path('homepage', views.homepage),
    #path('login', views.login),
    #path('logout', views.logout),
    
]