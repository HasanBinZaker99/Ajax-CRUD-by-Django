from django.contrib import admin
from App.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','email','occupation','gender','created_at']
    search_fields = ['name','email','occupation']
    list_filter = ['gender']
    list_per_page = 8
admin.site.register(Employee, EmployeeAdmin)

# Register your models here.
