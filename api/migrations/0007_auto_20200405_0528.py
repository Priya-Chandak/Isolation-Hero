# Generated by Django 3.0.3 on 2020-04-05 05:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_auto_20200404_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='BonusPointLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1024)),
                ('valid_till', models.DateTimeField()),
                ('points', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'BonusPointLinks',
            },
        ),
        migrations.AlterField(
            model_name='userdailystat',
            name='day',
            field=models.IntegerField(default=5),
        ),
        migrations.CreateModel(
            name='UserVisitBonusPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('bonus_point_link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.BonusPointLink')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'UserVisitBonusPoints',
            },
        ),
    ]