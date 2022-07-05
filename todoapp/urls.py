from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('<int:author_id>/', get_by_author_name),
    path('add/', TaskCreateView.as_view(), name='add_task'),
    
]
