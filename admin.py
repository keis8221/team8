from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .adminResources import TeacherResources
from .models import Teacher
from import_export.formats import base_formats

@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin):
    resource_class = TeacherResources
    formats = [base_formats.CSV]
# Register your models here.
