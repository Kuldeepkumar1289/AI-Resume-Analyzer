from django.urls import path
from .views import upload_resume, analyze_resume, download_report, history

urlpatterns = [
    path('', upload_resume, name='upload_resume'),
    path('api/analyze/', analyze_resume, name='analyze_resume'),
    path('download-report/', download_report, name='download_report'),
    path('history/', history, name='history'),
]