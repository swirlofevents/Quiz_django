# Generated by Django 2.2 on 2019-04-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0008_auto_20190425_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer',
            field=models.TextField(max_length=400, verbose_name='Ответ'),
        ),
    ]
