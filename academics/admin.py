from django.contrib import admin

from .models import (
    College,
    Department,
    Programme,
    Level,
    AcademicSession,
    Semester,
    Course,
)


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    search_fields = ("code", "name")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "college")
    list_filter = ("college",)
    search_fields = ("code", "name")


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ("degree", "name", "department", "duration")
    list_filter = ("degree", "department")
    search_fields = ("name",)


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ("name", "programme", "order")
    list_filter = ("programme",)


@admin.register(AcademicSession)
class AcademicSessionAdmin(admin.ModelAdmin):
    list_display = ("name", "is_current")
    list_editable = ("is_current",)


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ("session", "name")
    list_filter = ("session",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "title",
        "programme",
        "level",
        "semester",
        "credit_units",
        "course_type",
        "is_active",
    )

    list_filter = (
        "programme",
        "level",
        "semester",
        "course_type",
        "is_active",
    )

    search_fields = (
        "code",
        "title",
    )