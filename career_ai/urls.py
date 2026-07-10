from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from engine.views import upload_resume, download_report, history, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Root domain redirect karega login page par
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    path('upload/', upload_resume, name='upload'),
    path('history/', history, name='history'),
    path('download-report/', download_report, name='download_report'),
]