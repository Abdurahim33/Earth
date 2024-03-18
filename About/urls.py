from django.urls import path, include
from About.views import About_view

app_name = 'About'

urlpatterns = [
    path('About/', About_view.as_view(), name='About'),
]
