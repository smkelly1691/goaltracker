# Generated by Django 4.1.2 on 2022-10-31 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_goal_complete_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='complete_status',
        ),
        migrations.AddField(
            model_name='update',
            name='complete_status',
            field=models.BooleanField(default=False),
        ),
    ]
