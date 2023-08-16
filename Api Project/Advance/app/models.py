from django.db import models

# Create Model that take flipkart payload.
class Flipkart_Api(models.Model):
    Title = models.CharField(max_length=20)
    Price = models.IntegerField()
    Description = models.TextField()
    No_Of_Reviews_And_Ratings = models.IntegerField()
    Ratings = models.IntegerField()
    No_Of_Media_Counts_Present_Product_Box = models.IntegerField()
    
    def __str__(self):
        return self.Title