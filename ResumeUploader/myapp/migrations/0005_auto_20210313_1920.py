# Generated by Django 3.1.5 on 2021-03-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210313_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='prfile_image',
            field=models.ImageField(blank=True, upload_to='ProfileImg'),
        ),
    ]
