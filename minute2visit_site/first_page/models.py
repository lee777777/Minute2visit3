from django.db import models
from PIL import Image

class Tour(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="...")
    price_of_one = models.DecimalField(max_digits=10, decimal_places=2, default=50)
    price_of_2_to_4 = models.DecimalField(max_digits=10, decimal_places=2, default=50)
    price_of_5_to_9 = models.DecimalField(max_digits=10, decimal_places=2, default=50)
    price_of_10_to_15 = models.DecimalField(max_digits=10, decimal_places=2, default=50)
    price_of_16_to_20 = models.DecimalField(max_digits=10, decimal_places=2, default=50)
    picture = models.ImageField(upload_to='tour_pictures/', null=True)
 
    def __str__(self):
        return self.title   
    def save(self, *args, **kwargs):
       super().save()      
       img = Image.open(self.picture.path)
       if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.picture.path)


class Day(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='days')
    number_order = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.ImageField(upload_to='day_pictures/')
    
    def __str__(self):
        return f"Day {self.number_order}"
    
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

class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    PAX_CHOICES = [
    ("1", "Only one person"),
    ("2-4", "Two to four"),
    ("5-9", "Five to nine"),
    ("10-15", "Ten to fiften"),
    ("16-20", "Sixten to twenty"),
    ]
    num_pax =  models.CharField(
        max_length=10,
        choices=PAX_CHOICES,
        default="1",
    )
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking for {self.first_name} {self.last_name}"

class TermsAndConditions(models.Model):
    title = models.CharField(max_length=255)
    extra_information = models.TextField(null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Terms and Conditions"
        


class CancellationPolicy(models.Model):
    period = models.CharField(max_length=255)
    percentage = models.CharField(max_length=255, default="25% of the actual price")
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.period}, {self.percentage}"

    class Meta:
        verbose_name_plural = "Cancellation Policy"
 
 
        
class Included(models.Model):
    title = models.CharField(max_length=255)
    extra_information = models.TextField(null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Included Services"
  
  
    
class Excluded(models.Model):
    title = models.CharField(max_length=255)
    extra_information = models.TextField(null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Excluded Services"   