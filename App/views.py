from django.shortcuts import render
from App.models import Employee
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib import messages

# Function to render Homepage
def home(request):
    employ_list = Employee.objects.all().order_by('-created_at')
    return render(request,"home.html",{"employees":employ_list})

# JSON
def employee_json(request):
    employees = Employee.objects.all()
    data = [employee.get_data() for employee in employees]
    response = {'data': data}
    return JsonResponse(response)

# Function to ADD Employee
def add_employee(request):
    if request.method == "POST":
        if request.POST.get('name') \
            and request.POST.get('email') \
            and request.POST.get('occupation') \
            and request.POST.get('salary') \
            and request.POST.get('gender') \
            and request.POST.get('note'):
            employee = Employee()
            employee.name = request.POST.get('name')
            employee.email = request.POST.get('email')
            employee.occupation = request.POST.get('occupation')
            employee.salary = request.POST.get('salary')
            employee.gender = request.POST.get('gender')
            employee.note = request.POST.get('note')
            employee.save()
            messages.success(request,"Employee added successfully !")
            return HttpResponseRedirect("/")
        else:
            return render(request,'add.html')

# Function to View Employee data individually
def employee(request,employee_id):
    employee = Employee.objects.get(id = employee_id)
    if employee != None:
        return render(request,"edit.html",{'employee':employee})
# Function to Edit Employee
def edit_employee(request):
    if request.method == "POST":
        employee = Employee.objects.get(id = request.POST.get('id'))
        if employee != None:
            employee.name = request.POSST.get('name')
            employee.email = request.POSST.get('email')
            employee.occupation = request.POSST.get('occupation')
            employee.salary = request.POSST.get('salary')
            employee.gender = request.POSST.get('gender')
            employee.note = request.POSST.get('note')
            employee.save()
            messages.success(request,"Employee Updated Successfully !")
            return HttpResponseRedirect("/")

# Function to Delete Employee 
def delete_employee(request,employee_id):
    employee = Employee.objects.get(id = employee_id)
    employee.delete()
    messages.success(request,"Employee deleted successfully !")
    return HttpResponseRedirect("/")




def show_data(request):
    data = [{"date": "2020-08-10", "trade_code": "1JANATAMF", "high": "4.3", "low": "4.1", "open": "4.2", "close": "4.1", "volume": "2,285,416"}, {"date": "2020-08-09", "trade_code": "1JANATAMF", "high": "4.3", "low": "4.1", "open": "4.1", "close": "4.2", "volume": "1,292,933"}, {"date": "2020-08-06", "trade_code": "1JANATAMF", "high": "4.2", "low": "4.1", "open": "4.1", "close": "4.1", "volume": "2,653,824"}]

    # return JsonResponse(data,safe=False)
    return render(request,"data.html",{"data":data})

