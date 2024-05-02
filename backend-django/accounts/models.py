from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):
    """
    Create and return a superuser with the given email, username, first name, and password.

    :param email: Email address of the superuser.
    :param user_name: Username of the superuser.
    :param first_name: First name of the superuser.
    :param password: Password of the superuser.
    :param other_fields: Additional fields for the superuser (optional).
    :return: Created superuser object.
    """
       
    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        
        return self.create_user(email, user_name, first_name, password, **other_fields)
    
    def create_user(self, email, user_name, first_name, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
    

class NewUser(AbstractBaseUser, PermissionsMixin):
    """
    Create and return a regular user with the given email, username, first name, and password.

    :param email: Email address of the user.
    :param user_name: Username of the user.
    :param first_name: First name of the user.
    :param password: Password of the user.
    :param other_fields: Additional fields for the user (optional).
    :return: Created user object.
    """
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name',]

    def __str__(self) -> str:
        return self.user_name

        