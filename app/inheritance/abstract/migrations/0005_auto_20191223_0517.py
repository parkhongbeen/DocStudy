# Generated by Django 3.0 on 2019-12-23 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abstract', '0004_auto_20191220_0849'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instructor',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['name']},
        ),
    ]
