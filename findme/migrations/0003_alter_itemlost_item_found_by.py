# Generated by Django 3.2.6 on 2021-08-30 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('findme', '0002_itemlost_item_found_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemlost',
            name='item_found_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_found_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
