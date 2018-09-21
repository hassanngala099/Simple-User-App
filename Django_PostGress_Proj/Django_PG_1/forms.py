from django import forms
from django.contrib.auth.models import User
from . models import Topic

class SignupForm_Example(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','email','password']

class login_FormExample(forms.Form):
	username=forms.CharField(max_length=10)
	Password =forms.CharField(max_length=10)

class new_topic(forms.ModelForm):

	class Meta:
		model=Topic
		"""fields=_all_"""
		fields=['subject']
