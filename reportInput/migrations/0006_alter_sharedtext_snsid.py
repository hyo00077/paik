# Generated by Django 4.2 on 2022-10-06 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reportInput", "0005_alter_paragraph_headclass"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sharedtext",
            name="snsID",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]