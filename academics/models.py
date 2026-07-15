from django.db import models
from django.db import models


class College(models.Model):
    name = models.CharField(max_length=150, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    college = models.ForeignKey(
        College,
        on_delete=models.CASCADE,
        related_name="departments"
    )
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=10)

    class Meta:
        unique_together = ("college", "code")

    def __str__(self):
        return f"{self.name}"


class Programme(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="programmes"
    )
    name = models.CharField(max_length=150)

    duration = models.PositiveIntegerField(default=4)

    def __str__(self):
        return self.name


class AcademicSession(models.Model):
    name = models.CharField(max_length=20, unique=True)

    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Semester(models.Model):

    SEMESTERS = [
        ("First", "First"),
        ("Second", "Second"),
    ]

    session = models.ForeignKey(
        AcademicSession,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=20, choices=SEMESTERS)

    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.session} - {self.name}"


class Level(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Course(models.Model):

    code = models.CharField(max_length=20, unique=True)

    title = models.CharField(max_length=200)

    unit = models.PositiveIntegerField(default=3)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE
    )

    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE
    )

    lecturer = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"role": "lecturer"},
    )

    def __str__(self):
        return f"{self.code} - {self.title}"
# Create your models here.
