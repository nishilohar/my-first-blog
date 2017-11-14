from django.db import models

# Create your models here.


class Story(models.Model):
	name = models.CharField(max_length = 50)
	story_title = models.CharField(max_length = 100) 
	story = models.TextField()
	category = models.CharField(max_length = 20, null = True)
	last_updated = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.story_title