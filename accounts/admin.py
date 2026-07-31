from django.contrib import admin

from .models import (
    User,
    Student,
    Lecturer,
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "role",
        "is_active",
        "is_staff",
    )

    list_filter = (
        "role",
        "is_active",
        "is_staff",
        "is_superuser",
    )

    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email",
    )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "matric_number",
        "admission_number",
        "user",
        "programme",
        "level",
        "session",
        "status",
    )

    list_filter = (
        "programme",
        "level",
        "session",
        "status",
    )

    search_fields = (
        "matric_number",
        "admission_number",
        "user__username",
        "user__first_name",
        "user__last_name",
    )


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = (
        "staff_id",
        "user",
        "department",
        "rank",
        "qualification",
    )

    list_filter = (
        "department",
        "rank",
    )

    search_fields = (
        "staff_id",
        "user__username",
        "user__first_name",
        "user__last_name",
    )