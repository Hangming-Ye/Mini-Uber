from django.urls import path
from . import views

urlpatterns = [
    # example:
    path('user_reg/', views.user_reg),
    # path('homepage/', views.homepage),
    path('get_user_info/', views.get_user_info),
    path('login/', views.login),
    path('driver_form/', views.modify_driver),
    path('logout/', views.logout),
    path('driver_de_register/', views.driver_de_register),
]