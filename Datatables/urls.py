from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('show/',views.show_data,name='show_data'),
    path('json/',views.employee_json,name="employee_josn"),

    # Path to ADD Employee
    path('add_employee',views.add_employee,name='add_employee'),
    # Path to View Employee data individually
    path('employee/<str:employee_id',views.employee,name='employee'),
    # Path to Edit Employee
    path('edit_employee',views.edit_employee,name='edit_employee'),
    # Path to Delete Employee 
    path('delete_employee/<str:employee_id>',views.delete_employee,name='delete_employee')
]
