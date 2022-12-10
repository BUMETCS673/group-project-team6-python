# Generated by Django 4.1.3 on 2022-12-09 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("iGroup", "0001_initial"),
        ("survey", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="resultquestionscore",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="survey.question"
            ),
        ),
        migrations.AddField(
            model_name="resultquestionscore",
            name="result_team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="iGroup.resultteam"
            ),
        ),
        migrations.AddField(
            model_name="instance",
            name="instructor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="instances",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="configinstance",
            name="instance",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="iGroup.instance"
            ),
        ),
        migrations.AddField(
            model_name="configinstance",
            name="instructor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="configinstance",
            name="survey",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="survey.survey"
            ),
        ),
    ]
