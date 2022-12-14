# Generated by Django 4.0.6 on 2022-07-23 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lista', '0012_remove_film_price_ticket_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ordered_item',
            name='product',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='lista.ticket'),
        ),
    ]
