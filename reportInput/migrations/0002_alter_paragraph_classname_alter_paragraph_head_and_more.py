# Generated by Django 4.1.1 on 2022-10-03 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reportInput", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paragraph",
            name="className",
            field=models.CharField(
                blank=True,
                choices=[
                    ("indent", "indent"),
                    ("noindent", "noindent"),
                    ("narrow", "narrow"),
                    ("narrowindent", "narrowindent"),
                ],
                max_length=60,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="paragraph",
            name="head",
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name="paragraph",
            name="headClass",
            field=models.CharField(
                blank=True,
                choices=[("BoldnUnder", "BoldnUnder"), ("Bold", "Bold")],
                max_length=60,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="reportinputstring",
            name="textChar",
            field=models.CharField(
                blank=True, choices=[("p", "p"), ("h2", "h2")], max_length=2, null=True
            ),
        ),
    ]