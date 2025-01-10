from django.urls import path
from delivery import views

urlpatterns = [
    path('delivery_personnel_list/', views.delivery_personnel_list, name='delivery_personnel_list'),
    path('delivery_personnel_create_/',views.delivery_personnel_create_,name='delivery_personnel_create_'),
    path('delivery_personnel_update_/<int:id>/',views.delivery_personnel_update_,name='delivery_personnel_update_'),
    path('delivery_personnel_delete_/<int:id>',views.delivery_personnel_delete_,name='delivery_personnel_delete_'),
    path('meal_list/',views.meal_list,name='meal_list'),
    path('meal_preparation_create_/',views.meal_preparation_create_,name='meal_preparation_create_'),
    path('meal_preparation_update_/<int:id>/',views.meal_preparation_update_,name='meal_preparation_update_'),
    path('meal_preparation_delete_/<int:id>/',views.meal_preparation_delete_,name='meal_preparation_delete_'),

]
