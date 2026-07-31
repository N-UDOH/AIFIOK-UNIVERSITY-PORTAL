from django.db import models


# =====================================================
# COLLEGE
# =====================================================

class College(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


# =====================================================
# DEPARTMENT
# =====================================================

class Department(models.Model):
    college = models.ForeignKey(
        College,
        on_delete=models.CASCADE,
        related_name="departments"
    )

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)

    class Meta:
        ordering = ["name"]
        unique_together = ("college", "name")

    def __str__(self):
        return f"{self.name} ({self.college.code})"


# =====================================================
# PROGRAMME
# =====================================================

class Programme(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="programmes"
    )

    name = models.CharField(max_length=200)

    degree = models.CharField(
        max_length=20,
        choices=[
            ("BSc", "BSc"),
            ("MSc", "MSc"),
            ("PhD", "PhD"),
        ],
        default="BSc",
    )

    duration = models.PositiveIntegerField(default=4)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.degree} {self.name}"


# =====================================================
# LEVEL
# =====================================================

class Level(models.Model):
    programme = models.ForeignKey(
        Programme,
        on_delete=models.CASCADE,
        related_name="levels"
    )

    name = models.CharField(max_length=50)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ["order"]
        unique_together = ("programme", "name")

    def __str__(self):
        return f"{self.programme} - {self.name}"


# =====================================================
# ACADEMIC SESSION
# =====================================================

class AcademicSession(models.Model):
    name = models.CharField(max_length=20, unique=True)
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


# =====================================================
# SEMESTER
# =====================================================

class Semester(models.Model):
    session = models.ForeignKey(
        AcademicSession,
        on_delete=models.CASCADE,
        related_name="semesters"
    )

    name = models.CharField(
        max_length=20,
        choices=[
            ("First", "First"),
            ("Second", "Second"),
        ]
    )

    class Meta:
        unique_together = ("session", "name")

    def __str__(self):
        return f"{self.session} - {self.name} Semester"


# =====================================================
# COURSE
# =====================================================

class Course(models.Model):
    COURSE_TYPES = [
        ("Core", "Core"),
        ("Elective", "Elective"),
        ("GST", "GST"),
    ]

    programme = models.ForeignKey(
        Programme,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    code = models.CharField(max_length=20)

    title = models.CharField(max_length=255)

    credit_units = models.PositiveIntegerField(default=3)

    course_type = models.CharField(
        max_length=20,
        choices=COURSE_TYPES,
        default="Core",
    )

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["code"]
        unique_together = ("programme", "code")

    def __str__(self):
        return f"{self.code} - {self.title}"