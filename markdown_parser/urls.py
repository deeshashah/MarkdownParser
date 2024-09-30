from django.urls import path

from . import views

urlpatterns = [
    path('markdown/', views.markdown_to_html, name='markdown_to_html'),
]