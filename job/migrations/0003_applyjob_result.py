# Generated by Django 2.0 on 2019-09-25 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyjob',
            name='result',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='job.Result'),
            preserve_default=False,
        ),
    ]
