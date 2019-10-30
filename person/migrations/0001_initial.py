# Generated by Django 2.1.7 on 2019-05-25 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import house.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IdentityInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity_type', models.CharField(choices=[('KTP', 'KTP - Kartu Tanda Penduduk'), ('SIM', 'SIM - Surat Ijin Mengemudi'), ('KTM', 'KTM - Kartu Tanda Mahasiswa')], max_length=3, verbose_name='Jenis Identitas')),
                ('identity_number', models.CharField(max_length=50, verbose_name='Nomor Identitas')),
                ('identity_name', models.CharField(max_length=60, null=True, verbose_name='Nama Sesuai Identitas')),
                ('dob', models.DateField(verbose_name='Tanggal Lahir')),
                ('gender', models.CharField(choices=[('M', 'Pria'), ('F', 'Wanita')], max_length=1, verbose_name='Jenis Kelamin')),
                ('identity_address', models.CharField(max_length=100, null=True, verbose_name='Alamat Sesuai Identitas')),
                ('religion', models.CharField(choices=[('islam', 'Islam'), ('kristen', 'Kristen'), ('hindu', 'Hindu'), ('buddha', 'Buddha'), ('konghucu', 'Konghucu')], max_length=8, verbose_name='Agama')),
                ('marriage_status', models.CharField(choices=[('menikah', 'Menikah'), ('belum', 'Belum Menikah')], max_length=7, verbose_name='Status Perkawinan')),
                ('work', models.CharField(max_length=100, verbose_name='Pekerjaan')),
                ('phone', models.CharField(max_length=100, verbose_name='Phone')),
                ('is_renter', models.BooleanField(default=False, verbose_name='Penyewa')),
                ('is_owner', models.BooleanField(default=False, verbose_name='Pemilik')),
                ('identity_photo', models.ImageField(blank=True, null=True, upload_to=house.helpers.photo_path)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Username')),
            ],
        ),
    ]