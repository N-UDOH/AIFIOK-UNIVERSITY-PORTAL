from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User Model for AIFIOK University
    """

    ROLE_CHOICES = (
        ("admin", "Administrator"),
        ("lecturer", "Lecturer"),
        ("student", "Student"),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="student",
    )

    matric_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True,
        null=True,
    )

    staff_id = models.CharField(
        max_length=30,
        unique=True,
        blank=True,
        null=True,
    )

    college = models.CharField(
        max_length=100,
        blank=True,
    )

    department = models.CharField(
        max_length=100,
        blank=True,
    )

    level = models.CharField(
        max_length=10,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )

    def __str__(self):
        if self.first_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
# Create your models here.
