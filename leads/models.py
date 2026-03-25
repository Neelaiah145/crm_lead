from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

# Create your models here.


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be is_superuser=True")

        return self.create_user(email, password, **extra_fields)




class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=12)
    

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'   
    REQUIRED_FIELDS = ['name'] 

    def __str__(self):
        return self.email


















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
        
        