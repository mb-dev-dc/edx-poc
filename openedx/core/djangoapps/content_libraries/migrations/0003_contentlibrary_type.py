# Generated by Django 2.2.15 on 2020-08-25 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_libraries', '0002_group_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentlibrary',
            name='type',
            field=models.CharField(choices=[('video', 'Video'), ('complex', 'Complex'), ('problem', 'Problem')], default='complex', max_length=25),
        ),
    ]