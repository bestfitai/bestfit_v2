# Generated by Django 3.0.1 on 2020-01-03 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestfit', '0002_user_info_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]