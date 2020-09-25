from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


#creates a new form that enherits from the user creation form

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    #Meta gives us the nested namespace for configurations and keeps
    #configurations in the same place
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
#update username  
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
 #update profile image      
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']