from django import forms
from django.contrib.auth.models import User
from .models import Profile
# from .models import Course

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label = 'password', widget = forms.PasswordInput)
	password2 = forms.CharField(label = 'Repeat Password', widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Password didn\'t matched')
		return cd['password2']


class UserEditForm(forms.ModelForm):
		class Meta:
			model = User
			fields = ('username', 'first_name', 'email') 


class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile	
		fields = ('address', 'photo') 			