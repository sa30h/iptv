from django.db import models

# Create your models here.
class Url(models.Model):
	url_id=models.CharField(max_length=20,primary_key=True)
	name=models.CharField(max_length=50)
	url=models.CharField(max_length=100)

	def __str__(self):
		return self.url_id

