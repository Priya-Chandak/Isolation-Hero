# Generated by Django 3.0.3 on 2020-04-04 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_auto_20200401_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlocationhistory',
            name='reason',
        ),
        migrations.RemoveField(
            model_name='userlocationhistory',
            name='unique_group_code',
        ),
        migrations.RemoveField(
            model_name='userlocationhistory',
            name='verified',
        ),
        migrations.AlterField(
            model_name='userdailystat',
            name='day',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='userlevelscore',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='custom_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userlocationhistory',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]