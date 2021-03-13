from django.db import models
from django.forms import ModelForm
from django.forms.models import model_to_dict

# Create your models here.

class Office(models.Model):
    name = models.CharField(max_length=20)
    locations = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

    def natural_key(self):
        print("natural keys--office")
        return model_to_dict(self)

    # def natural_key(self):
    #     return (model_to_dict(self))
    

    

    



class Employee(models.Model):

    gender=[
        ("M","Male"),
        ("F","Female")

    ]


    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)    
    email = models.EmailField(max_length=254)
    gender=models.CharField(max_length=20,choices=gender)
    office=models.ForeignKey(Office, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
        
    # def natural_key(self):
    #     return (model_to_dict(self))
    
    


class OfficeForm(ModelForm):
    class Meta:
        model = Office
        fields = "__all__"

    
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

