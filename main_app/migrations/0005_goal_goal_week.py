# Generated by Django 4.1.2 on 2022-11-03 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_goal_completed_at_remove_goal_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='goal_week',
            field=models.IntegerField(default=1),
        ),
    ]
