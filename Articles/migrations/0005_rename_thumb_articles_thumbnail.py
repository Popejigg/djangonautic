# Generated by Django 3.2.5 on 2022-02-25 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0004_articles_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='thumb',
            new_name='thumbnail',
        ),
    ]
