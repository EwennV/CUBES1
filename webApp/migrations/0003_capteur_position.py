# Generated by Django 4.2.5 on 2023-10-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0002_remove_capteur_name_capteur2'),
    ]

    operations = [
        migrations.AddField(
            model_name='capteur',
            name='position',
            field=models.CharField(default='maison', max_length=64),
            preserve_default=False,
        ),
    ]
