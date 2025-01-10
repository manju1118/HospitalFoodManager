from django.urls import path
from pantry import views

urlpatterns = [
    path('staff/', views.pantry_staff_list, name='pantry_staff_list'),
    path('pantry_staff_create_/',views.pantry_staff_create_,name='pantry_staff_create_'),
    path('get_pantry_detail/<int:id>/',views.get_pantry_detail,name='get_pantry_detail'),
    path('staff_update/<int:id>/',views.staff_update,name='staff_update'),
    path('staff_delete/<int:id>/',views.staff_delete,name='staff_delete'),
]
