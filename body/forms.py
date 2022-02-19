from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from . models import Country, Currency, UserRoles, UnitsOfMeasurement
from django import forms
 
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password' )
#class UserProfileForm(forms.ModelForm):
 #   class Meta:
  #      model = UserProfile
  #      fields = ('Name', 'Surname','Cell','BirthDate','UserRoleId' )

class CreateUserRolesForm(forms.ModelForm):
    class Meta:
        model = UserRoles
        fields = ('id','Role', )
class CreateCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('id','Name','FlagPicture', )

class CreateCurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ('CountryId','RateToUsd','CurrencySymbol', )

class CreateUnitsOfMeasurementForm(forms.ModelForm):
    class Meta:
        model = UnitsOfMeasurement
        fields = ('UnitName','RatioToMetric','MesurementSymbol', )