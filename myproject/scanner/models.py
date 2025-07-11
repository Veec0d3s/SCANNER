from django.db import models
import uuid

class Device(models.Model):
    DEVICE_CATEGORIES = [
        ('printer', 'Printer'),
        ('monitor', 'Monitor'),
        ('cpu', 'CPU'),
        ('ups', 'UPS'),
        ('laptop', 'Laptop'),
        # add more as needed
    ]

    STATUS_CHOICES = [
        ('functional', 'Functional'),
        ('non_functional', 'Non Functional'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    BRAND_CHOICES = [
        ('dell', 'Dell'),
        ('hp', 'HP'),
        ('lenovo', 'Lenovo'),
        # add more brands as needed
    ]

    device_id = models.CharField(max_length=50, unique=True, editable=False, blank=True)
    category = models.CharField(max_length=20, choices=DEVICE_CATEGORIES)
    assigned = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='no')
    assigned_to = models.CharField(max_length=100, blank=True, null=True)
    room_number = models.CharField(max_length=50, blank=True, null=True)
    block = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='functional',
        blank=False,
        null=False,
    )
    serial_number = models.CharField(max_length=100, blank=True)
    tag_number = models.CharField(max_length=100, blank=True)
    date_acquired = models.DateField(blank=True, null=True)
    engraved = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='no')
    engravement_number = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES, default='dell')

    def save(self, *args, **kwargs):
        if not self.device_id:
            self.device_id = str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.device_id} - {self.category} - {self.brand}"
