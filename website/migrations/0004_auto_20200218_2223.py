# Generated by Django 3.0.3 on 2020-02-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200218_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(),
        ),
    ]
