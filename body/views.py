from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from sqlalchemy import false
from.forms import CreateCurrencyForm, RegistrationForm,LoginForm,CreateUserRolesForm,CreateCountryForm,CreateUnitsOfMeasurementForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from  .models import  UserRoles as UserRoles_Model
from  .models import Country as Country_Model
from . models import Currency as Currency_Model
from . models import UnitsOfMeasurement as Measurement_Model
from django.contrib.auth.models import User

from . serializers import RegistrationSerializer
from rest_framework import viewsets
# Create your views here.
class Api_RegistrationView(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('id')
    
    serializer_class = RegistrationSerializer

def RegistrationView(request):
  

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('CreateProfile')
    else:
        form = RegistrationForm()
    return render(request, 'Accounts/RegistrationPage.html', {'form': form})


#def CreateProfileView(request):
 #   if request.method == 'POST':
 #       form = UserProfileForm(request.POST)
 #       if form.is_valid():
 #           UserProfile.objects.create()
 #           return redirect('Login')
 #   else:
  #      form = UserProfileForm()
 #   return render(request, 'Accounts/CreateProfilePage.html', {'form': form})

    
def LoginView(request):

    if request.user.is_authenticated:
        return redirect('Dashboard')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('Dashboard')
        else:
            form = LoginForm()
            return render(request,'Accounts/LoginPage.html',{'form':form})
     
    else:
        form = LoginForm()
    return render(request, 'Accounts/LoginPage.html', {'form':form})


def dashboardView(request):
    
        

    return render(request, "dashboardPage.html",  {})






#USER ROLES
def UserRolesView(request):
  
    RolesList = UserRoles_Model.objects.all()
    Context = {
       
        'RolesList':RolesList,

    }
    return render(request, "CreateBasics/UserRoles/Details.html",  Context)

def CreateUserRoleView(request):

    context ={}
 

    form = CreateUserRolesForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"You have successfully created a user role")
        return redirect("UserRoles")
    context['form']= form
    return render(request, "CreateBasics/UserRoles/Create.html", context)
 
def DeleteUserRoleView(request, id ):

    context ={}
    Obj = UserRoles_Model.objects.filter(id = id)

    if request.method =="POST":
        Obj.delete()
        messages.success(request,"You have successfully deleted a user role")
        return redirect("UserRoles") 
    return render(request, "CreateBasics/UserRoles/delete.html", context)

def UpdateUserRoleView(request, id):
    context ={}
    obj = get_object_or_404(UserRoles_Model, id = id)
    form = CreateUserRolesForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        messages.success(request,"You have successfully updated a user role")
        return redirect("UserRoles")
    context["form"] = form
    return render(request, "CreateBasics/UserRoles/Update.html", context)






#Country

def CountryView(request):
  
    CountryList = Country_Model.objects.all()
    Context = {
       
        'CountryList':CountryList,

    }
    return render(request, "CreateBasics/Countries/Details.html",  Context)

def CreateCountryView(request):
    if request.method == 'POST':
        form = CreateCountryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            
            return redirect("Countries")
    else:
        form = CreateCountryForm()
        return render(request, 'CreateBasics/Countries/Create.html', {'form': form})
  

 
def DeleteCountryView(request, id ):

    context ={}
    Obj = Country_Model.objects.filter(id = id)

    if request.method =="POST":
        Obj.delete()
        messages.success(request,"You have successfully deleted a Country")
        return redirect("Countries") 
    return render(request, "CreateBasics/Countries/delete.html", context)

def UpdateCountryView(request, id):
    context ={}
    obj = get_object_or_404(Country_Model, id = id)
    form = CreateCountryForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        messages.success(request,"You have successfully Updated a Country")
        return redirect("Countries")
    context["form"] = form
    return render(request, "CreateBasics/Countries/Update.html", context)




#Currency

def CurrencyView(request):
  
    CurrencyList = Currency_Model.objects.all()
    Context = {
       
        'CurrencyList':CurrencyList,

    }
    return render(request, "CreateBasics/Currency/Details.html",  Context)

def CreateCurrencyView(request):

    context ={}
 

    form = CreateCurrencyForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"You have successfully created a currency")
        return redirect("Currency")
    context['form']= form
    return render(request, "CreateBasics/Currency/Create.html", context)
 
def DeleteCurrencyView(request, id ):

    context ={}
    Obj = Currency_Model.objects.filter(id = id)

    if request.method =="POST":
        Obj.delete()
        messages.success(request,"You have successfully deleted a currency")
        return redirect("Currency") 
    return render(request, "CreateBasics/Currency/delete.html", context)

def UpdateCurrencyView(request, id):
    context ={}
    obj = get_object_or_404(Currency_Model, id = id)
    form = CreateCurrencyForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        messages.success(request,"You have successfully updated a currency")
        return redirect("Currency")
    context["form"] = form
    return render(request, "CreateBasics/Currency/Update.html", context)


# unit of mesurement 
def MesurementView(request):
  
    MesurementList = Measurement_Model.objects.all()
    Context = {
       
        'MesurementList':MesurementList,

    }
    return render(request, "CreateBasics/Mesurement/Details.html",  Context)

def CreateMesurementView(request):

    context ={}
 

    form = CreateUnitsOfMeasurementForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"You have successfully created a mesurement")
        return redirect("Mesurement")
    context['form']= form
    return render(request, "CreateBasics/Mesurement/Create.html", context)
 
def DeleteMesurementView(request, id ):

    context ={}
    Obj = Measurement_Model.objects.filter(id = id)

    if request.method =="POST":
        Obj.delete()
        messages.success(request,"You have successfully deleted a mesurement")
        return redirect("Mesurement") 
    return render(request, "CreateBasics/Mesurement/delete.html", context)

def UpdateMesurementView(request, id):
    context ={}
    obj = get_object_or_404(Measurement_Model, id = id)
    form = CreateUnitsOfMeasurementForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        messages.success(request,"You have successfully updated a mesurement")
        return redirect("Mesurement")
    context["form"] = form
    return render(request, "CreateBasics/Mesurement/Update.html", context)