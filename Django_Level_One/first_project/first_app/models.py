from django.db import models

# Create your models here.

class Topic(models.Model):
	top_name = models.CharField(max_length=264,unique=True)
	def __str__(self):
		return self.top_name
		
	on_delete=models.CASCADE
	 	

class Webpage(models.Model):

	topic = models.ForeignKey(Topic,on_delete=models.CASCADE,related_name="tags",related_query_name="tag",)
	name = models.CharField(max_length=264,unique= True)
	url  =models.URLField(unique=True)

	def __str__(self):
		return self.name
	on_delete=models.CASCADE

class AccessRecord(models.Model):
	name = models.ForeignKey(Webpage,on_delete=models.CASCADE,related_name="tags",related_query_name="tag",)
	date = models.DateField()

	def __str__(self):
		return str(self.date) 
	on_delete=models.CASCADE