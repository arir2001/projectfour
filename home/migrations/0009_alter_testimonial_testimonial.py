# Generated by Django 4.2.15 on 2024-08-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_testimonial_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='testimonial',
            field=models.TextField(blank=True, max_length=140),
        ),
    ]
