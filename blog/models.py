from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): #This line defines our model. It is an object
		STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published'), # You can either draft or publish your blog post.

		)
		author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) # ForignKey is a link to another model
		title = models.CharField(max_length = 200)
		text = models.TextField()
		created_date = models.DateTimeField(default = timezone.now) #Indicates when the post was created
		published_date = models.DateTimeField(blank = True, null = True) # Indicates when the post was published
		publish = models.DateTimeField(default = timezone.now)# Indicates when the post was published

		class Meta:
				ordering = ('-publish',) # Order by the most recent post

		def __str__(self):
				return self.title # When we call str method, we get a text(str) with a Post title