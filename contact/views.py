from django.shortcuts import render
from . import forms
# Create your views here.

def contact(request):
	title = "contact us"
	confirm_message = None
	form = forms.ContactForm(request.POST or None)
	if form.is_valid():
		name = form.cleaned_data.get('name')
		email = form.cleaned_data.get('email')
		message = form.cleaned_data.get('message')

		title = None
		form = None
		confirm_message = "Thanks for reaching out."
	context = {
		'form':form,
		'title':title,
		'confirm_message':confirm_message
	}
	return render(request, "contact.html",context)