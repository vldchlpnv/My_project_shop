# Generated by Django 5.1 on 2024-09-13 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_instrumentscatalog_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['slug']},
        ),
    ]
