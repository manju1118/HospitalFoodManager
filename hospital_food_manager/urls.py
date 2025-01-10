from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hospital/', include('hospital.urls')),
    path('pantry/', include('pantry.urls')),
    path('delivery/', include('delivery.urls')),
    path('auth_app/',include('auth_app.urls')),
]
