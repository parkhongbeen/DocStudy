# Generated by Django 3.0 on 2019-12-20 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abstract', '0002_auto_20191220_0843'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instructor',
            options={'ordering': ['age']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['age']},
        ),
    ]
