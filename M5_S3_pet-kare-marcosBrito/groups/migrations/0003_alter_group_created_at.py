# Generated by Django 4.2.5 on 2023-10-03 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_alter_group_pet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
