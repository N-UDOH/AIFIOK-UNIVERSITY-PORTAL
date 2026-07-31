from django.db import models
from django.contrib.auth.models import AbstractUser


# =====================================================
# CUSTOM USER
# =====================================================

class User(AbstractUser):

    ROLE_CHOICES = [
        ("admin", "Administrator"),
        ("lecturer", "Lecturer"),
        ("student", "Student"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="student",
    )

    def __str__(self):
        return self.username


# =====================================================
# STUDENT PROFILE
# =====================================================

class Student(models.Model):

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Deferred", "Deferred"),
        ("Graduated", "Graduated"),
        ("Suspended", "Suspended"),
        ("Withdrawn", "Withdrawn"),
    ]

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile",
    )

    matric_number = models.CharField(
        max_length=30,
        unique=True,
    )

    admission_number = models.CharField(
        max_length=30,
        unique=True,
    )

    programme = models.ForeignKey(
        "academics.Programme",
        on_delete=models.PROTECT,
    )

    level = models.ForeignKey(
        "academics.Level",
        on_delete=models.PROTECT,
    )

    session = models.ForeignKey(
        "academics.AcademicSession",
        on_delete=models.PROTECT,
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
    )

    date_of_birth = models.DateField()

    nationality = models.CharField(
        max_length=100,
        default="Nigeria",
    )

    state_of_origin = models.CharField(
        max_length=100,
    )

    address = models.TextField()

    phone_number = models.CharField(
        max_length=20,
    )

    parent_name = models.CharField(
        max_length=200,
    )

    parent_phone = models.CharField(
        max_length=20,
    )

    parent_email = models.EmailField(
        blank=True,
    )

    admission_date = models.DateField()

    passport = models.ImageField(
        upload_to="students/",
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active",
    )

    def __str__(self):
        return f"{self.matric_number} - {self.user.get_full_name()}"


# =====================================================
# LECTURER PROFILE
# =====================================================

class Lecturer(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="lecturer_profile",
    )

    staff_id = models.CharField(
        max_length=30,
        unique=True,
    )

    department = models.ForeignKey(
        "academics.Department",
        on_delete=models.PROTECT,
    )

    office = models.CharField(
        max_length=200,
        blank=True,
    )

    rank = models.CharField(
        max_length=100,
    )

    qualification = models.CharField(
        max_length=100,
    )

    specialization = models.CharField(
        max_length=200,
        blank=True,
    )

    employment_date = models.DateField()

    phone_number = models.CharField(
        max_length=20,
    )

    passport = models.ImageField(
        upload_to="lecturers/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.staff_id} - {self.user.get_full_name()}"