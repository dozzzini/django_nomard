# Generated by Django 4.2.3 on 2023-08-08 02:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0006_alter_room_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='amenities',
            field=models.ManyToManyField(related_name='rooms', to='rooms.amenity'),
        ),
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='categories.category'),
        ),
        migrations.AlterField(
            model_name='room',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]
