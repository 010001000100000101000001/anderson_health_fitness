from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg


class GearCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    overview = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Gear Categories"

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class GearItem(models.Model):
    category = models.ForeignKey(GearCategory, related_name='gear_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    details = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    weight = models.CharField(max_length=20, null=True, blank=True)
    material_type = models.CharField(max_length=100, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image_file = models.ImageField(upload_to='gear_images/', null=True, blank=True)
    highlight = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return self.name

class ProductReview(models.Model):
    gear_item = models.ForeignKey(GearItem, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # Rating between 1-5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('gear_item', 'user')  # Prevents multiple reviews from the same user on the same item
        ordering = ['-created_at']  # Newest reviews first

    def __str__(self):
        return f'Review by {self.user.username} on {self.gear_item.name}'

# Signals to update the average rating of GearItem when reviews are created, updated, or deleted
@receiver(post_save, sender=ProductReview)
@receiver(post_delete, sender=ProductReview)
def update_gear_item_rating(sender, instance, **kwargs):
    gear_item = instance.gear_item
    reviews = ProductReview.objects.filter(gear_item=gear_item)
    if reviews.exists():
        gear_item.rating = reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
    else:
        gear_item.rating = None  # Set to None if no reviews exist
    gear_item.save()