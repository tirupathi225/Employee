"""Employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employeeapp import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^register/',views.register,name='register'),
    url(r'^user_login/',views.user_login,name='user_login'),
    url(r'^logout/',views.user_logout,name='logout'),
    url(r'^list',views.EmployeeListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.EmployeeDetailView.as_view(),name='detail'),
    url(r'^(?P<pk>\d+)/update$', views.EmployeeUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete$', views.EmployeeDeleteView.as_view(), name='delete'),





]
