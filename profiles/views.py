from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse


from . import forms
from . import models

# Create your views here.
def add_new_story(request):
	title = "Tell Your Story To The World"
	form = forms.AddStoryForm(request.POST or None)
	confirm_message = None
	if form.is_valid():
		var = models.Story.objects.create(
				name = form.cleaned_data['name'],
				story_title = form.cleaned_data['story_title'],
				story = form.cleaned_data['story'],
				category = form.cleaned_data['category']
			)
		# form.save()
		form = None
		title = None
		confirm_message = "Thanks for sharing story"

	context = {
		'title':title,
		'form':form,
		'confirm_message':confirm_message
	}
	return render(request,"profiles/add_story.html",context)

def sign_up(request):
	form = forms.SignUpForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username = username, password = raw_password)
			login(request, user)
			return redirect("/")
		else:
			print ("invalid form ")
			form = forms.SignUpForm()
			print (type(form))
	return render(request, "profiles/signup.html",{'form':form})	



def log_in(request):
	username = password = ""
	# form = forms.LogInForm(request.POST or None)
	print ("in login")
	if request == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			print ("successfully logged in")
			return redirect("/")
		else:
			return HttpResponse("invalid login")
	return render(request, "profiles/login.html")