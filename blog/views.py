from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404
from profiles import models as profile_models
# Create your views here.
def index(request):
	latest_blog_list = profile_models.Story.objects.order_by('-last_updated')[:5]
	template = "blog/index.html"
	context = {
		'latest_blog_list':latest_blog_list
	}
	return render(request,template,context)


def detail(request, blog_id):
	questionDetail = get_object_or_404(profile_models.Story,pk = blog_id)
	template = "blog/full-blog-content.html"
	context = {
		'questionDetail':questionDetail
	}
	return render(request, template,context)

def category(request, category_type):
	if category_type == "more":
		print ("category is more")
		all_categories = get_list_or_404(profile_models.Story.objects.values('category').distinct())
		print (">>>>>>>>>>>>>>>>>>>>>>")
		print (all_categories)
		context = {
			'all_categories' : all_categories
		}
	else:
		category_questions = get_list_or_404(profile_models.Story, category__icontains=category_type)
		context = {
			'category_questions': category_questions
		}
	
	template = "blog/category.html"
	return render(request,template, context)