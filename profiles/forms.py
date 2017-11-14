from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



from . import models

class AddStoryForm(forms.ModelForm):
	class Meta:
		model = models.Story
		fields = (
			'name',
			'story_title',
			'story',
			'category'
			)


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length = 30, required = False, help_text = "Optional")
	surname = forms.CharField(max_length = 30, required = False, help_text = "Optional")
	email = forms.EmailField(max_length = 254, help_text = "Inform a valid email address")

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'surname',
			'email',
			'password1',
			'password2'
			)

class LogInForm(forms.ModelForm):
	class Meta:
		model = User
		fields = (
			'username',
			'password',
			)