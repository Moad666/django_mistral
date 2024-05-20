from django.urls import path
from .views import generate_text, analyze_context

urlpatterns = [
    path('generate/', generate_text, name='generate_text'),
    path('analyze_context/', analyze_context, name='analyze_context'),
]