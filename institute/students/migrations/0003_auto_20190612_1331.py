# Generated by Django 2.2.2 on 2019-06-12 08:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20190611_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='sem',
        ),
        migrations.AddField(
            model_name='student',
            name='branch',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='s_id',
            field=models.IntegerField(),
        ),
    ]
