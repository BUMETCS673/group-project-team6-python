# Generated by Django 3.2 on 2022-11-09 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('survey', '0001_initial'),
        ('iGroup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configinstance',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.survey'),
        ),
    ]
