# Generated by Django 4.2.4 on 2023-10-04 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]