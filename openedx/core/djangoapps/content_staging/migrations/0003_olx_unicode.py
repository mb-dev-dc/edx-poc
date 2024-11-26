# Generated by Django 3.2.23 on 2023-12-07 20:10

from django.db import migrations
import openedx_learning.lib.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content_staging', '0002_stagedcontentfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stagedcontent',
            name='display_name',
            field=openedx_learning.lib.fields.MultiCollationCharField(db_collations={'mysql': 'utf8mb4_unicode_ci', 'sqlite': 'NOCASE'}, max_length=768),
        ),
        migrations.AlterField(
            model_name='stagedcontent',
            name='olx',
            field=openedx_learning.lib.fields.MultiCollationTextField(db_collations={'mysql': 'utf8mb4_bin', 'sqlite': 'BINARY'}),
        ),
    ]