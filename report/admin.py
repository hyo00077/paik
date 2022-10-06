from django.contrib import admin
from .models import Report, ReportImage, ReportString
from django.utils.html import format_html

# Register your models here.


class adminReportImage(admin.StackedInline):
    list_display = ("id", "report", "image_tag")
    readonly_fields = ('image_tag',)

    model = ReportImage


class adminReportText(admin.StackedInline):
    list_display = ("id", "report", "text")

    model = ReportString


class adminReport(admin.ModelAdmin):
    list_display = ("id", "koTitle", "image_tag", "created_at", "updated_at")
    readonly_fields = ('image_tag', "created_at", "updated_at")
    inlines = [adminReportImage, adminReportText]

    class Meta:
        model = Report

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        for img in request.FILES.getlist('photos_multiple'):
            obj.image_set.create(image_url=img)
        for text in request.FILES.getlist('text_multiple'):
            obj.text_set.create(string=text)


admin.site.register(Report, adminReport)
# admin.site.register(ReportImage, adminReportImage)
