from . import views
from django.urls import path

urlpatterns = [
    path('', views.AddNewEmployee.as_view()),
    path('done/', views.done),
    path('employees/', views.show_all_employees),
    path('employee/<int:pk>/', views.ShowOneEmployee.as_view(), name='employee_detail'),
]
