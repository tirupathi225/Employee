from django.shortcuts import render
from employeeapp.forms import UserForm,EmployeeForm
from employeeapp.models import Employee
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView,)


# Create your views here.

def index(request):
    return render(request,'employeeapp/index.html')

def register(request):

    registered=False

    if request.method=='POST':

        user_form=UserForm(data=request.POST)
        profile_form=EmployeeForm(data=request.POST)
        #import pdb; pdb.set_trace()
        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            print(user, 'gsfsfs')

            user.set_password(user.password)

            user.save()

            profile=profile_form.save(commit=False)

            profile.user=user

            if 'profile_pic' in request.FILES:
                print('found it')

                profile.profile_pic=request.FILES['profile_pic']

            profile.save()


            resitered=True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=EmployeeForm()


    return render(request,'employeeapp/registration.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})


@login_required
def special(request):
    return HttpResponse("You are logged in ")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')
        #import pdb; pdb.set_trace()
        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('list'))
            else:
                return HttpResponse("Your account is not active")
        else:
            print("Someone tried to login and failed")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request,'employeeapp/login.html',{})


# Create your views here.
class EmployeeListView(ListView):
    context_object_name = 'employees'
    model = Employee

class EmployeeDetailView(DetailView):
    context_object_name = 'employee_detail'
    model = Employee

class EmployeeUpdateView(UpdateView):
    fields = ('Name', 'age')
    model = Employee
    success_url = reverse_lazy('list')


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('list')
