from django.contrib import admin
from .models import ReportInput, ReportInputString, SharedText, Paragraph
import nested_admin
# Register your models here.


class adminSharedText(admin.ModelAdmin):
    list_display = ("id", "sentence", "snsChoices", "snsID", "created_at")
    readonly_fields = ("created_at", )

    class Meta:
        model = SharedText


class adminReportText(nested_admin.NestedStackedInline):
    list_display = ("id", "report", "text")
    model = ReportInputString

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        for img in request.FILES.getlist('photos_multiple'):
            obj.image_set.create(image_url=img)
        for text in request.FILES.getlist('text_multiple'):
            obj.text_set.create(string=text)


class adminParagraph(nested_admin.NestedStackedInline):
    list_display = ("id", "report", "className")
    model = Paragraph
    inlines = [adminReportText]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        for img in request.FILES.getlist('photos_multiple'):
            obj.image_set.create(image_url=img)
        for text in request.FILES.getlist('text_multiple'):
            obj.text_set.create(string=text)


class adminReportInput(nested_admin.NestedModelAdmin):
    list_display = ("id", "koTitle", "image_tag", "created_at", "updated_at")
    readonly_fields = ('image_tag', "created_at", "updated_at")
    inlines = [adminParagraph]

    class Meta:
        model = ReportInput

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        for img in request.FILES.getlist('photos_multiple'):
            obj.image_set.create(image_url=img)
        for text in request.FILES.getlist('text_multiple'):
            obj.text_set.create(string=text)


admin.site.register(ReportInput, adminReportInput)
admin.site.register(SharedText, adminSharedText)
