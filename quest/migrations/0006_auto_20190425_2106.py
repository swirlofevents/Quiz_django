# Generated by Django 2.2 on 2019-04-25 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0005_auto_20190425_2101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='question_text',
            new_name='question',
        ),
    ]