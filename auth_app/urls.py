from django.urls import path

from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_page,name='login'),
    path('register/',views.register_page,name='register'),
    path('logout/',views.user_logout,name='logout'),
]
