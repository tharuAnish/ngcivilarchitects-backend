# Generated by Django 4.2.2 on 2023-07-18 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_remove_course_c_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='c_tags',
            field=models.CharField(help_text='Comma-separated tags', max_length=120, null=True),
        ),
    ]
