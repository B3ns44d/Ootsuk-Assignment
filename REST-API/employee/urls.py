
from django.urls import path
from .api import EmployeeCreateApi, EmployeeApi, EmployeeUpdateApi, EmployeeDeleteApi

urlpatterns = [
    path('ootsuk', EmployeeApi.as_view()),
    path('ootsuk/create',EmployeeCreateApi.as_view()),
    path('ootsuk/<int:pk>',EmployeeUpdateApi.as_view()),
    path('ootsuk/<int:pk>/delete',EmployeeDeleteApi.as_view()),
]
