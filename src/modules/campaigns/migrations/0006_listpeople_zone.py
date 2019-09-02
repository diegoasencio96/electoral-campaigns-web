# Generated by Django 2.2.4 on 2019-09-01 17:22

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('campaigns', '0005_auto_20190825_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='listpeople',
            name='zone',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='city', chained_model_field='city', default=1, on_delete=django.db.models.deletion.CASCADE, to='locations.Zone', verbose_name='Zona o comuna'),
            preserve_default=False,
        ),
    ]
