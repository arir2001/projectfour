# Generated by Django 4.2.15 on 2024-08-18 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_testimonial_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='extra_detail',
            field=models.CharField(default='Manager', max_length=100, unique=True),
        ),
    ]
