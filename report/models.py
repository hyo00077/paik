from django.db import models

# Create your models here.


class Report(models.Model):
    koTitle = models.CharField(max_length=50)
    thumbNail = models.ImageField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.koTitle

    def image_tag(self):
        from django.utils.html import format_html
        return format_html("<img src='{url}' width= 200px height= 300px object-fit= scale-down>".format(url=self.thumbNail.url))
        image_tag.short_description = 'Image'
        image_tag.allow_tags = True


class ReportImage(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return f'{self.pk}_[{self.report.koTitle}]'

    def image_tag(self):
        from django.utils.html import format_html
        return format_html("<img src='{url}' width= 200px height= 300px object-fit= scale-down>".format(url=self.image.url))
        image_tag.short_description = 'Image'
        image_tag.allow_tags = True


class ReportString(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=30, null=True, blank=True)
    text = models.CharField(max_length=500, null=False, blank=False)
