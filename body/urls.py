from django.urls import path,include
from .  import views as body_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Register', body_views.Api_RegistrationView)

urlpatterns = [
    #API Url
    path('api/', include(router.urls)),
   

    #Authencication
    path('', body_views.RegistrationView, name='Registration'),
   # path('UserProfile', body_views.dashboardView, name='dashboard'),
    path('Login', body_views.LoginView, name='Login'),
    #Dashboard
    path('dashboard', body_views.dashboardView, name='Dashboard'),
    #settings | USER ROLES
    path('dashboard/userRoles', body_views.UserRolesView, name='UserRoles'),
    path('dashboard/userRoles/Create', body_views.CreateUserRoleView, name='CreateUserRole'),
    path('dashboard/userRoles<id>Delete', body_views.DeleteUserRoleView, name='DeleteUserRole'),
    path('dashboard/userRoles<id>Update', body_views.UpdateUserRoleView, name='UpdateUserRole'),
    # Setting | COUNTRY
    path('dashboard/country', body_views.CountryView, name='Countries'),
    path('dashboard/country/Create', body_views.CreateCountryView, name='CreateCountry'),
    path('dashboard/country<id>Delete', body_views.DeleteCountryView, name='DeleteCountry'),
    path('dashboard/country<id>Update', body_views.UpdateCountryView, name='UpdateCountry'),
    # Setting | Currency 
    path('dashboard/currency', body_views.CurrencyView, name='Currency'),
    path('dashboard/currency/Create', body_views.CreateCurrencyView, name='CreateCurrency'),
    path('dashboard/currency<id>Delete', body_views.DeleteCurrencyView, name='DeleteCurrency'),
    path('dashboard/currency<id>Update', body_views.UpdateCurrencyView, name='UpdateCurrency'),
    # Setting | Mesurement 
    path('dashboard/mesurement', body_views.MesurementView, name='Mesurement'),
    path('dashboard/mesurement/Create', body_views.CreateMesurementView, name='CreateMesurement'),
    path('dashboard/mesurement<id>Delete', body_views.DeleteMesurementView, name='DeleteMesurement'),
    path('dashboard/mesurement<id>Update', body_views.UpdateMesurementView, name='UpdateMesurement'),
]