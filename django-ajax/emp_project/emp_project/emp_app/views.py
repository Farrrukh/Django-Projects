from django.shortcuts import render
from .models import OfficeForm,EmployeeForm,Office,Employee
from django.http import JsonResponse, QueryDict
from django.core import serializers
from django.forms.models import model_to_dict
import json

# Create your views here.

def home(request):
    officeForm = OfficeForm()
    employeeForm = EmployeeForm()
    context = {
        "officeForm" : officeForm , 
        "employeeForm" : employeeForm
    }
    return render(request , 'index.html',  context=context)

    
def OfficeCrud(request):
    if request.method == "POST":

        print(request.POST)
        officeForm = OfficeForm(request.POST)
        office=officeForm.save()

        # return JsonResponse(serializers.serialize("json",[office]),safe=False)
        return JsonResponse(model_to_dict(office),safe=False)
def changeEmployeeToJson(employee):
    office = employee.office
    print(office)
    officeJson = model_to_dict(office)
        
    response = model_to_dict(employee)
    response['office'] = officeJson
    return response

def EmployeeCrud(request):
    if request.method == "POST":
        employeeForm=EmployeeForm(request.POST)
        employee=employeeForm.save()
        response=changeEmployeeToJson(employee)

        return JsonResponse(response)

    if request.method == "PUT":
        print(request.body)
        data = json.loads(request.body)
        data['office'] = Office(id = data.get('office'))
        del data['csrfmiddlewaretoken']
        employee = Employee(**data)
        print(employee)
        response = {}
        employee.save()
        response = changeEmployeeToJson(employee)
        return JsonResponse(response)



def getAllOffices(request):

    office=Office.objects.all()
    return JsonResponse(serializers.serialize("json",office),safe=False)


def getAllEmployee(request):

    employees = Employee.objects.all()
    data = serializers.serialize("json" , employees , use_natural_foreign_keys=True)
    return JsonResponse( data , safe=False)
def showEmployeePage(request):
    
    employeeForm = EmployeeForm()
    context = {
        
        "employeeForm" : employeeForm
    }
    return render(request ,template_name="employee-page.html" , context = context)

def showOfficePage(request):
    officeForm = OfficeForm()
   
    context = {
        "officeForm" : officeForm 
        
    }
    return render(request ,template_name="office-page.html" , context=context)


