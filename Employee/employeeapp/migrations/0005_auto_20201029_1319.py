# Generated by Django 3.1 on 2020-10-29 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employeeapp', '0004_auto_20201029_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=80)),
                ('age', models.IntegerField()),
                ('salary', models.FloatField()),
                ('position', models.CharField(choices=[('l1', 'level 1'), ('l2', 'level 2'), ('l3', 'level 3'), ('l4', 'level 4'), ('l5', 'level 5'), ('l6', 'level 6'), ('l7', 'level 7'), ('l8', 'level 8'), ('l9', 'level 9'), ('l10', 'level 10')], max_length=50)),
                ('address', models.CharField(max_length=80)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
