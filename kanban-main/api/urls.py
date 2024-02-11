from api.views import DetailTask, ListTask #,NewUserForm

from django.urls import path
from . import views
urlpatterns = [
    path('tasks/', ListTask.as_view()),
    path('task/<str:pk>', DetailTask.as_view()),
]
