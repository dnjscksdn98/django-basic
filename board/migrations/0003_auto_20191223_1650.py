# Generated by Django 3.0.1 on 2019-12-23 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_board_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='tag',
            new_name='tags',
        ),
    ]
