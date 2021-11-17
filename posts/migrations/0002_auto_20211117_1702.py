# Generated by Django 3.1.4 on 2021-11-17 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='added_by',
            field=models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser'),
        ),
    ]
