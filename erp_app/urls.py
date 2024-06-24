from django.urls import path
from .views import home,register,admin_dashboard,doctor_validate,doctor_login,doctor_dashboard

urlpatterns = [
    path('register/',register,name='register'),
    path('admin_dashboard/',admin_dashboard,name='admin_dashboard'),
    path('home/',home,name='home'),
    path('doctor_validate/',doctor_validate,name='doctor_validate'),
    path('doctor_login/',doctor_login,name='doctor_login'),
    path('doctor_dashboard/',doctor_dashboard,name='doctor_dashboard')

]