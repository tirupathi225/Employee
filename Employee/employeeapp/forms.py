from django import forms
from django.contrib.auth.models import User
from employeeapp.models import Employee

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model=User
        fields=('username','email','password')



class EmployeeForm(forms.ModelForm):
    class Meta():
        model=Employee
        fields=('Name', 'age', 'salary', 'position', 'address')
