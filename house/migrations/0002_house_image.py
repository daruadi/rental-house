# Generated by Django 3.1.4 on 2021-02-14 07:21

from django.db import migrations, models
import house.models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=house.models.house_dir),
        ),
    ]
