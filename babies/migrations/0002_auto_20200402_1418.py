# Generated by Django 3.0.4 on 2020-04-02 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('babies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baby',
            name='time_of_birth',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='baby',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]