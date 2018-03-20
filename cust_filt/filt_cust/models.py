from django.db import models

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length = 30)
	company = models.CharField(max_length =30)
	amount = models.PositiveIntegerField(null=True, blank=True)

	def __str__(self):
		return str(self.name)