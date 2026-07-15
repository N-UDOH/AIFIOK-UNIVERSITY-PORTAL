from django.contrib import admin

from .models import (
    College,
    Department,
    Programme,
    AcademicSession,
    Semester,
    Level,
    Course,
)

admin.site.register(College)
admin.site.register(Department)
admin.site.register(Programme)
admin.site.register(AcademicSession)
admin.site.register(Semester)
admin.site.register(Level)
admin.site.register(Course)