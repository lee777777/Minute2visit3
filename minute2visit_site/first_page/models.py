from django.db import models
from PIL import Image

class Tour(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to='tour_pictures/')
    
    def save(self, *args, **kwargs):
       super().save()
       img = Image.open(self.picture.path)
       if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)


class Day(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='days')
    number_order = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.ImageField(upload_to='day_pictures/')
    
    def save(self, *args, **kwargs):
       super().save()
       img = Image.open(self.picture.path)
       if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)
            
    class Meta:
        unique_together = ('tour', 'number_order')
        ordering = ('number_order',)



class TermsAndConditions(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Terms and Conditions"
        


class CancellationPolicy(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Cancellation Policy"
 
 
        
class Included(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
  
  
    
class Excluded(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title