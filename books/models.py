from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Book(models.Model):
	title = models.TextField()
	genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
	# when the vendor model is created
	# vendor = models.ForeignKey("vendor", on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=7, decimal_places=2) # decimal field to accurately store currency
	image = CloudinaryField("image")
	author = models.CharField(max_length=256)
	isbn = models.CharField(max_length=13)
	book_summary = models.TextField()


class Genre(models.Model):
	pass