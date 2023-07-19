# Generated by Django 4.2.2 on 2023-07-18 01:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='c_point1',
        ),
        migrations.RemoveField(
            model_name='course',
            name='c_point2',
        ),
        migrations.RemoveField(
            model_name='course',
            name='c_point3',
        ),
        migrations.RemoveField(
            model_name='course',
            name='c_type',
        ),
        migrations.RemoveField(
            model_name='course',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='course',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='course',
            name='c_content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='c_overview',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='c_desc',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
