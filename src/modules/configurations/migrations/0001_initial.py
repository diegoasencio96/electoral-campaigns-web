# Generated by Django 2.2.4 on 2019-08-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticalParty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Nombre del partido')),
                ('icon', models.ImageField(upload_to='political_party_icon/', verbose_name='Logo del partido')),
            ],
            options={
                'verbose_name': 'Partido político',
                'verbose_name_plural': 'Partidos políticos',
            },
        ),
    ]
