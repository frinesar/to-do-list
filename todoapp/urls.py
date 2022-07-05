from django.urls import path, include
from .views import *


urlpatterns = [
    path('', TasksListView.as_view(), name='index'),
    path('task/<int:pk>/', TaskDetailView.as_view()),
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('update/<int:pk>', TaskUpdateView.as_view(), name='update'),
    # path('<int:pk>/delete', TaskDeleteView.as_view(), name='delete_task'),
    
]
