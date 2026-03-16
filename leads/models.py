from django.db import models

# Create your models here.

class Contact_lead(models.Model):
        STATUS_CHOICES = (
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('interest', 'interest'),
        ('closed', 'closed'),
    )
        name = models.CharField(max_length=100)
        phone_number = models.CharField( max_length=15, blank=True, null=True)
        email = models.EmailField()
        message = models.TextField()
        status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='new')
        created_at = models.DateTimeField(auto_now_add=True)
        
        