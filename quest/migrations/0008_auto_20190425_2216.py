# Generated by Django 2.2 on 2019-04-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0007_auto_20190425_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer',
            field=models.CharField(max_length=400, verbose_name='Ответ'),
        ),
    ]
