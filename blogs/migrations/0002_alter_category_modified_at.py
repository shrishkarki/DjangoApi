# Generated by Django 4.0.5 on 2022-07-09 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='modified_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]