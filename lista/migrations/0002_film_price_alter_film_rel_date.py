# Generated by Django 4.0.6 on 2022-07-09 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='price',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='film',
            name='rel_date',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
