# Generated by Django 4.0.6 on 2022-07-23 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0011_rename_name_ticket_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='price',
        ),
        migrations.AddField(
            model_name='ticket',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]