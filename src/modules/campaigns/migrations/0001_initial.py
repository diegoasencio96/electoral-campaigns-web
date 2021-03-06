# Generated by Django 2.2.4 on 2019-08-25 18:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configurations', '0001_initial'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='campaigns/images/', verbose_name='Imagen de la campaña')),
                ('name', models.CharField(max_length=180, verbose_name='Nombre del candidato')),
                ('number', models.CharField(max_length=3, verbose_name='Número en el tarjetón')),
                ('political_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.PoliticalParty', verbose_name='Partido politico')),
            ],
            options={
                'verbose_name': 'Candidatura',
                'verbose_name_plural': 'Candidatura',
            },
        ),
        migrations.CreateModel(
            name='CampaignCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Nombre del cargo')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Orden')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='campaigns.CampaignCharge', verbose_name='Cargo del que se deriva')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='ListPeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_list', models.PositiveIntegerField(blank=True, null=True, verbose_name='Número de la planilla')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de la planilla')),
                ('ubication', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ubicación')),
                ('city', smart_selects.db_fields.ChainedForeignKey(chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='locations.City', verbose_name='Municipio')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.Country', verbose_name='País')),
                ('state', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country', chained_model_field='country', on_delete=django.db.models.deletion.CASCADE, to='locations.Region', verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Planilla',
                'verbose_name_plural': 'Planillas',
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de la reunión')),
                ('start_time', models.TimeField(verbose_name='Hora de inicio de la reunión')),
                ('end_time', models.TimeField(verbose_name='Hora de finalización de la reunión')),
                ('esteemed_assistants', models.PositiveIntegerField(blank=True, null=True, verbose_name='Número de asistentes esperados')),
                ('address', models.CharField(max_length=180, verbose_name='Dirección')),
                ('number_chairs', models.PositiveIntegerField(blank=True, null=True, verbose_name='Número de sillas')),
                ('number_tables', models.PositiveIntegerField(blank=True, null=True, verbose_name='Número de mesas')),
                ('number_snacks', models.PositiveIntegerField(blank=True, null=True, verbose_name='Número de refrigerios')),
                ('number_gifts', models.PositiveIntegerField(blank=True, null=True, verbose_name='Número de regalos')),
                ('observations', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('candidature', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='campaigns.Campaign', verbose_name='Candidatura')),
                ('city', smart_selects.db_fields.ChainedForeignKey(chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='locations.City', verbose_name='Municipio')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.Country', verbose_name='País')),
                ('sector', smart_selects.db_fields.ChainedForeignKey(chained_field='zone', chained_model_field='zone', on_delete=django.db.models.deletion.CASCADE, to='locations.Neighborhood', verbose_name='Sector o barrio')),
                ('state', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country', chained_model_field='country', on_delete=django.db.models.deletion.CASCADE, to='locations.Region', verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Reunion o actividad',
                'verbose_name_plural': 'Actividades',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=180, null=True, verbose_name='Nombres')),
                ('last_name', models.CharField(blank=True, max_length=180, null=True, verbose_name='Apellidos')),
                ('sex', models.CharField(blank=True, choices=[('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otro')], max_length=1, null=True, verbose_name='Sexo')),
                ('year_old', models.PositiveIntegerField(blank=True, null=True, verbose_name='Edad')),
                ('identification_card', models.CharField(max_length=15, verbose_name='Cédula')),
                ('cellphone', models.CharField(blank=True, max_length=10, null=True, verbose_name='Celular')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Correo electrónico')),
                ('address', models.CharField(max_length=180, verbose_name='Dirección')),
                ('is_voter', models.BooleanField(default=False, verbose_name='¿Es votante?')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Orden')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('campaign_charge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='campaigns.CampaignCharge', verbose_name='Cargo en la campaña')),
                ('city', smart_selects.db_fields.ChainedForeignKey(chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='locations.City', verbose_name='Municipio')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.Country', verbose_name='País')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='TypeMeeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Tipo de actividad')),
            ],
            options={
                'verbose_name': 'Tipo de actividad',
                'verbose_name_plural': 'Tipos de actividades',
            },
        ),
        migrations.CreateModel(
            name='Surveyed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaigns.ListPeople', verbose_name='Planilla')),
                ('meeting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='campaigns.Meeting', verbose_name='Actividad')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaigns.Person', verbose_name='Persona')),
            ],
            options={
                'verbose_name': 'Encuestado',
                'verbose_name_plural': 'Encuestados',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='list_people',
            field=models.ManyToManyField(blank=True, through='campaigns.Surveyed', to='campaigns.ListPeople', verbose_name='Planillas'),
        ),
        migrations.AddField(
            model_name='person',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='campaigns.Person', verbose_name='Persona a cargo'),
        ),
        migrations.AddField(
            model_name='person',
            name='sector',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='zone', chained_model_field='zone', null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.Neighborhood', verbose_name='Sector o barrio'),
        ),
        migrations.AddField(
            model_name='person',
            name='state',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country', chained_model_field='country', on_delete=django.db.models.deletion.CASCADE, to='locations.Region', verbose_name='Departamento'),
        ),
        migrations.AddField(
            model_name='person',
            name='voting_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='locations.VotingPost', verbose_name='Puesto de votación'),
        ),
        migrations.AddField(
            model_name='person',
            name='zone',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='city', chained_model_field='city', null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.Zone', verbose_name='Zona'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='type_activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='campaigns.TypeMeeting', verbose_name='Tipo de actividad'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='zone',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='city', chained_model_field='city', on_delete=django.db.models.deletion.CASCADE, to='locations.Zone', verbose_name='Zona'),
        ),
    ]
