# Generated by Django 4.2.3 on 2023-08-12 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='desc',
            field=models.CharField(default='school description', max_length=255),
            preserve_default=False,
        ),
    ]