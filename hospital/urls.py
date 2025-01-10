from django.urls import path
from hospital import views

urlpatterns = [
    path('patients/', views.patient_list_, name='patient_list_create'),
    path('patient_create_/',views.patient_create_,name='patient_create_'),
    path('patient_detail/<int:id>/',views.patient_detail,name='patient_detail'),
    path('patient_update/<int:id>/',views.patient_update,name='patient_update'),
    path('patients/<int:id>/', views.patient_detail, name='patient_detail'),
    path('patient_delete/<int:id>/',views.patient_delete,name='patient_delete'),
    path('diet-charts/', views.dietchart_list_, name='diet_chart_list_create'),
    path('diet/<int:id>/', views.dietchart_detail, name='dietchart_detail'),
    path('dietchart_create_/',views.dietchart_create_,name='dietchart_create_'),
    path('dietchart_update/<int:id>/',views.dietchart_update,name='dietchart_update'),
    path('dietchart_delete/<int:id>/',views.dietchart_delete,name='dietchart_delete'),
]
