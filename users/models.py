from django.db import models
from django.contrib.auth.models import AbstractUser
from easy_thumbnails.fields import ThumbnailerImageField
import uuid

class User(AbstractUser):
	id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	little_about_you = models.TextField(max_length=500, blank=True)
	profile_picture =ThumbnailerImageField(upload_to='profile_picture',
		default="no-picture.png")
	############# IF A USER CAN POST OR NOT ###############
	can_post = models.BooleanField(default=False)