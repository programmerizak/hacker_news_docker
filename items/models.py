from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
import uuid, datetime, django


class ItemManager(models.Manager):

	# # Filter new items 
	def new_items(self):
		# Calculate the time threshold (5 minutes ago)
		time_threshold = timezone.now() - timezone.timedelta(minutes=5)
		# Filter items created within the last 5 minutes
		recent_items = self.filter(item_type='topstories',
			date_created__gte=time_threshold)
		return recent_items


	# Filter past items
	def past_items(self):
		# Calculate the time threshold (5 minutes ago)
		time_threshold = timezone.now() - timezone.timedelta(minutes=5)
		# Filter items created before the last 5 minutes
		recent_items = self.filter(item_type='topstories',
			date_created__lt=time_threshold)
		return recent_items


	# Filter jobstories items
	def jobstories(self):
		return self.filter(item_type='jobstories')

	# Filter topstories items
	def topstories(self):
		return self.filter(item_type='topstories')

	# Filter askstories items
	def askstories(self):
		return self.filter(item_type='askstories')

	# Filter showstories items
	def showstories(self):
		return self.filter(item_type='showstories')


	# Filter show items
	def comments(self):
		return self.filter(item_type='comment')



class Item(models.Model):
	id = models.UUIDField(primary_key=True,default=uuid.uuid4,
		editable=False)
	# Am using this field to identify objects from the api
	api_item_id = models.CharField(max_length=100,
		blank=True,editable=False)
	title = models.CharField(max_length=250,blank=True)
	url = models.URLField(blank=True)
	text = models.TextField(blank=True)
	item_type = models.CharField(max_length=100)
	item_creator = models.CharField(max_length=100,blank=True)
	score = models.BigIntegerField(default=0, null=True)
	date_created = models.DateTimeField(default=django.utils.timezone.now)
	# date_created = models.DateTimeField(default=timezone.now())
	is_api_post = models.BooleanField(default=False)
	############ KIDS FOR THE COMMENTS 
	parent_item = models.ForeignKey('self', null=True, blank=True,
		on_delete=models.CASCADE, related_name='kid_items')
	objects = ItemManager()


	class Meta:
		ordering = ['-date_created',]

	def __str__(self):
		return self.title

	@property
	def no_comments(self):
		return self.kid_items.count()