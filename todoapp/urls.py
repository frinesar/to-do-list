from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index),
    path('<int:author_id>/', get_by_author_name),
    
]
