# Generated by Django 5.1.2 on 2024-10-16 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startit_app', '0011_alter_addresesq_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='image_url',
            field=models.URLField(blank=True, default='', max_length=500, verbose_name='Вставьте изображение'),
        ),
    ]
