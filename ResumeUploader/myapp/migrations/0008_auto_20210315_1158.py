# Generated by Django 3.1.5 on 2021-03-15 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('myapp', '0007_candidateuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='job_city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='CandidateUser',
        ),
    ]
