# Generated by Django 2.2.4 on 2019-08-26 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_meeting_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaigncharge',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='campaigns.Campaign', verbose_name='Campaña o candidatura'),
        ),
        migrations.AddField(
            model_name='typemeeting',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='campaigns.Campaign', verbose_name='Campaña o candidatura'),
        ),
    ]
