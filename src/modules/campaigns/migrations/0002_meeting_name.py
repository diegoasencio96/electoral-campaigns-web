# Generated by Django 2.2.4 on 2019-08-25 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='name',
            field=models.CharField(default=1, max_length=180, verbose_name='Nombre de la actividad actividad'),
            preserve_default=False,
        ),
    ]
