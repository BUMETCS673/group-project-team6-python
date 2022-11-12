# Generated by Django 3.2 on 2022-11-09 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigInstance',
            fields=[
                ('config_id', models.AutoField(primary_key=True, serialize=False)),
                ('max_num_pass', models.IntegerField()),
                ('num_group', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ResultInstance',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('instance', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='iGroup.configinstance')),
            ],
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('instance_id', models.AutoField(primary_key=True, serialize=False)),
                ('instance_name', models.CharField(max_length=256)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='configinstance',
            name='instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iGroup.instance'),
        ),
        migrations.AddField(
            model_name='configinstance',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
