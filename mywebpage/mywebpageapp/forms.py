from .models import Contact,Ass,Assignment1
from django import forms
from .models import UserProfileInfo,User
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
      class Meta:
          model = Contact
          exclude = ('',)

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment1
        exclude = ('',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        exclude = ('',)
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         exclude = ('',)


