# Generated by Django 2.1.5 on 2020-02-15 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]