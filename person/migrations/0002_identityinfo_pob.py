# Generated by Django 2.1.7 on 2019-06-11 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='identityinfo',
            name='pob',
            field=models.CharField(max_length=60, null=True, verbose_name='Tempat Kelahiran'),
        ),
    ]