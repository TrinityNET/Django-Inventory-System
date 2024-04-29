"""
URL configuration for inventory_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.user_login, name='login'),
    path('django_admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('equipment/', views.equipment, name='equipment'),
    path('make_reservation/<int:equipment_id>/', views.make_reservation, name='make_reservation'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservation/<int:pk>/delete/', views.delete_reservation, name='delete_reservation'),
    path('admin/', views.admin, name='admin'),
    path('logout/', views.user_logout, name='logout'),
]
