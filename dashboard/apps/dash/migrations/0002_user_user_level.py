# Generated by Django 4.2.3 on 2023-08-27 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_level',
            field=models.IntegerField(default=9),
            preserve_default=False,
        ),
    ]