# Generated by Django 5.0.6 on 2024-05-31 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_producto_carbs_alter_producto_fat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.image'),
        ),
    ]
