from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Board(models.Model):
	name=models.CharField(max_length=30,unique=True)
	description=models.CharField(max_length=30)

	
	def __str__(self):
		return self.name

	

class Topic(models.Model):
	subject=models.CharField(max_length=30,null=False)
	last_updated=models.DateTimeField(auto_now_add=True)
	child_board=models.ForeignKey(Board,related_name='Small_Board',on_delete=models.CASCADE,)
	Topic_Beginner=models.ForeignKey(User,on_delete=models.CASCADE,)

	def __str__(self):
		return self.subject

class Post(models.Model):
	message=models.TextField(max_length=100)
	topic=models.ForeignKey(Topic,on_delete=models.CASCADE,)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_by=models.ForeignKey(User,null=True,related_name='+',on_delete=models.CASCADE,)

	def __str__(self):
		return self.message

