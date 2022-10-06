from random import choices
from django.db import models

# Create your models here.

# 리포트 하나


class ReportInput(models.Model):
    koTitle = models.CharField(max_length=50)
    enTitle = models.CharField(max_length=50)
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


# 공유 가능한 개별문장 모델

class Paragraph(models.Model):
    report = models.ForeignKey(
        ReportInput, related_name="report", on_delete=models.CASCADE)
    paraClass_choices = (
        ("reportPara", "reportPara"),
        ("hr", "hr")
    )
    paraClass = models.CharField(
        choices=paraClass_choices, max_length=60, default=paraClass_choices[0][0])

    class_name_choices = (
        ("indent", "indent"),
        ("noindent", "noindent"),
        ("narrow", "narrow"),
        ("narrowindent", "narrowindent"),
    )
    className = models.CharField(
        choices=class_name_choices, max_length=60, null=True, blank=True)
    head = models.CharField(max_length=60, null=True, blank=True)
    head_class_choices = (
        ("BoldnUnder", "BoldnUnder"),
        ("Bold", "Bold"),
        ("narrowNum", "narrowNum")
    )
    headClass = models.CharField(
        choices=head_class_choices, max_length=60, null=True, blank=True, default=head_class_choices[1][0])


class ReportInputString(models.Model):
    text_choices = (
        ("p", "p"),
        ("h2", "h2")
    )
    report = models.ForeignKey(
        Paragraph, related_name="report_text", on_delete=models.CASCADE)
    text = models.CharField(max_length=500, null=True, blank=True)
    textChar = models.CharField(
        choices=text_choices, max_length=2, null=True, blank=True)

    def __str__(self):
        return self.report.report.koTitle+" "+str(self.id)+"번째"

# 공유한 문장 수


class SharedText(models.Model):
    sns_choices = (
        ("twitter", "twitter"),
        ("instagram", "instagram"),
        ("facebook", "facebook")
    )
    snsChoices = models.CharField(choices=sns_choices, max_length=20)
    snsID = models.CharField(max_length=50, null=True, blank=True)
    sentence = models.ForeignKey(
        ReportInputString, related_name="text_shared", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return str(self.pk)+" "+str(self.sentence.report)
