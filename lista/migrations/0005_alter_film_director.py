# Generated by Django 4.0.6 on 2022-07-13 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0004_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lista.director'),
        ),
    ]
