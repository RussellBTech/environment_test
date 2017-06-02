from django.db import models

#Creates Item class so that we can create objects with the fields described here
class Item(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	amount = models.IntegerField()
