from django.urls import path, include
from .forms import LoginForm
from .views import *


urlpatterns = [
    path('login/', TaskLoginView.as_view(authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('', TasksListView.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view()),
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
    
]
