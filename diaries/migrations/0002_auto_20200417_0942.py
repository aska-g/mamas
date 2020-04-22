# Generated by Django 3.0.4 on 2020-04-17 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='diary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='diaries.Diary'),
        ),
    ]