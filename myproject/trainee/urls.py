from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_trainees, name='all_trainees'),
    path('create/', views.create_trainee, name='create_trainee'),
    path('<int:id>/', views.trainee_detail, name='trainee_detail'),
    path('<int:id>/update/', views.update_trainee, name='update_trainee'),
    path('<int:id>/delete/', views.delete_trainee, name='delete_trainee'),
]
