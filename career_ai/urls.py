from django.contrib import admin
from django.urls import path
from engine.views import upload_resume, download_report, history
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', upload_resume, name='home'),

    path('history/', history, name='history'),   

    path('download-report/', download_report, name='download_report'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]