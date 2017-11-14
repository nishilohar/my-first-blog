from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(max_length = 50, required = True)
	email = forms.EmailField(required = True)
	message = forms.CharField(max_length = 300, required = True)