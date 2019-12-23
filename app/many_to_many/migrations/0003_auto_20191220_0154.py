# Generated by Django 3.0 on 2019-12-20 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('clubs', models.ManyToManyField(through='many_to_many.Career', to='many_to_many.Club')),
            ],
        ),
        migrations.AddField(
            model_name='career',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='many_to_many.Club'),
        ),
        migrations.AddField(
            model_name='career',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='many_to_many.Player'),
        ),
    ]
