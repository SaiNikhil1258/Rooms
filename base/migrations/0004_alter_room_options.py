# Generated by Django 4.2 on 2024-03-12 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_content_message_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
