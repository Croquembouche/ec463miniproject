from django.db import models
import datetime

# Create your models here.

class Humidity(models.Model):
	humidity = models.DecimalField(max_digits=5, decimal_places=2)
	datetime_recorded = models.DateTimeField('datetime_recorded')

	def __str__(self):
		return str(self.humidity)

	def timeAdded(self):
		humidity = models.ForeignKey(Humidity, on_delete = models.CASCADE)
		self.datetime_recorded = datetime.datetime.now()
		return self.datetime_recorded

class Temperature(models.Model):
	temperature = models.DecimalField(max_digits=5, decimal_places=2)
	datetime_recorded = models.DateTimeField('datetime recorded')

	def __str__(self):
		return str(self.temperature)

	def timeAdded(self):
		self.datetime_recorded = datetime.datetime.now()
		return self.datetime_recorded