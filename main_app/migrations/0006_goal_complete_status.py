# Generated by Django 4.1.2 on 2022-10-31 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_reward_alter_update_options_alter_goal_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='complete_status',
            field=models.BooleanField(default=False),
        ),
    ]
