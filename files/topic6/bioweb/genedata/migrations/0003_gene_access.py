# Generated by Django 3.0.3 on 2020-08-05 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genedata', '0002_auto_20200805_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='gene',
            name='access',
            field=models.IntegerField(default=0),
        ),
    ]
