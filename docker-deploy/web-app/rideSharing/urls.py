from django.urls import path
from . import views

urlpatterns = [
    # example:
    path('register', views.user_reg),
    path('login', views.login),
    path('logout', views.logout),

]