# Generated by Django 4.2.6 on 2023-11-29 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='wikipedia_link',
            field=models.URLField(default='https://example.com'),
            preserve_default=False,
        ),
    ]
