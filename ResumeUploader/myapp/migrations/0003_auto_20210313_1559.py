# Generated by Django 3.1.5 on 2021-03-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210313_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='prfile_image',
            field=models.ImageField(blank=True, upload_to='ProfileImg'),
        ),
    ]
