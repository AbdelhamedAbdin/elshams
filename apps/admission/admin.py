from django.contrib import admin
from . import models


class AdmissionAdmin(admin.ModelAdmin):
    list_display = ["id", "child_name", "date"]
    list_filter = ["october_age", "is_joined_before", "siblings_count"]
    search_fields = ["international_id", "address", "birth_date", "email", "child_name"]


admin.site.register(models.Admission, AdmissionAdmin)
admin.site.register(models.Notification)
