from django.urls import path
from django.conf import settings
from .views import EmployeeDetail

urlpatterns = [
    path('emp', EmployeeDetail.as_view(), name = 'emp')
   
]
