from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from smart_selects.db_fields import ChainedForeignKey
from ..locations.models import City, Zone, Country, Region, Neighborhood, VotingPost
from ..configurations.models import PoliticalParty
import monolith.strings as strings
from django.utils import timezone

# Create your models here.


class Campaign(models.Model):
    image = models.ImageField(verbose_name='Imagen de la campaña', upload_to='campaigns/images/')
    name = models.CharField(max_length=180, verbose_name='Nombre del candidato')
    number = models.CharField(max_length=3, verbose_name='Número en el tarjetón')
    political_party = models.ForeignKey(PoliticalParty, verbose_name='Partido politico', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Candidatura'
        verbose_name_plural = 'Candidatura'

    def save(self, *args, **kwargs):
        super(Campaign, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)


class CampaignCharge(MPTTModel):
    campaign = models.ForeignKey(Campaign, verbose_name='Campaña o candidatura',
                                 null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=180, verbose_name='Nombre del cargo')
    order = models.PositiveIntegerField(verbose_name='Orden', default=0, blank=False, null=False)
    parent = TreeForeignKey('self', verbose_name='Cargo del que se deriva', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['order']

    def save(self, *args, **kwargs):
        super(CampaignCharge, self).save(*args, **kwargs)
        CampaignCharge.objects.rebuild()

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def save(self, *args, **kwargs):
        super(CampaignCharge, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)


class TypeMeeting(models.Model):
    name = models.CharField(max_length=180, verbose_name='Tipo de actividad')
    campaign = models.ForeignKey(Campaign, verbose_name='Campaña o candidatura',
                                 null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Tipo de actividad'
        verbose_name_plural = 'Tipos de actividades'

    def save(self, *args, **kwargs):
        super(TypeMeeting, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)


class Meeting(models.Model):
    id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.PROTECT)
    candidature = models.ForeignKey(Campaign, verbose_name='Candidatura', on_delete=models.PROTECT)
    name = models.CharField(max_length=180, verbose_name='Nombre de la actividad actividad')
    # voter_form = models.ManyToManyField(VoterForm, verbose_name='Planillas')
    date = models.DateField(verbose_name='Fecha de la reunión',  default=timezone.now)
    start_time = models.TimeField(verbose_name='Hora de inicio de la reunión')
    end_time = models.TimeField(verbose_name='Hora de finalización de la reunión')
    type_activity = models.ForeignKey(TypeMeeting, verbose_name='Tipo de actividad', null=True, blank=True,
                                      on_delete=models.CASCADE)
    esteemed_assistants = models.PositiveIntegerField(verbose_name='Número de asistentes esperados', null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name='País', on_delete=models.CASCADE)
    state = ChainedForeignKey(Region, verbose_name='Departamento',
                              chained_field='country', chained_model_field='country',
                              show_all=False, auto_choose=True)
    city = ChainedForeignKey(City, verbose_name='Municipio', chained_field='state', chained_model_field='state')
    zone = ChainedForeignKey(Zone, verbose_name='Zona', chained_field='city', chained_model_field='city')
    sector = ChainedForeignKey(Neighborhood, verbose_name='Sector o barrio', chained_field='zone', chained_model_field='zone')
    address = models.CharField(max_length=180, verbose_name='Dirección')
    number_chairs = models.PositiveIntegerField(verbose_name='Número de sillas', null=True, blank=True)
    number_tables = models.PositiveIntegerField(verbose_name='Número de mesas', null=True, blank=True)
    number_snacks = models.PositiveIntegerField(verbose_name='Número de refrigerios', null=True, blank=True)
    number_gifts = models.PositiveIntegerField(verbose_name='Número de regalos', null=True, blank=True)
    observations = models.TextField(verbose_name='Observaciones', null=True, blank=True)

    class Meta:
        verbose_name = 'Reunion o actividad'
        verbose_name_plural = 'Actividades'

    def save(self, *args, **kwargs):
        super(Meeting, self).save(*args, **kwargs)

    def __str__(self):
        return '{} | {}'.format(self.name, self.type_activity)


class ListPeople(models.Model):
    campaign = models.ForeignKey(Campaign, verbose_name='Campaña o candidatura',
                                 null=True, blank=True, on_delete=models.CASCADE)
    id_list = models.PositiveIntegerField(verbose_name='Número de la planilla', null=False, blank=False)
    date = models.DateField(verbose_name='Fecha de la planilla', default=timezone.now)
    country = models.ForeignKey(Country, verbose_name='País', on_delete=models.CASCADE)
    state = ChainedForeignKey(Region, verbose_name='Departamento', chained_field='country', chained_model_field='country',
                              show_all=False, auto_choose=True)
    city = ChainedForeignKey(City, verbose_name='Municipio', chained_field='state', chained_model_field='state')
    ubication = models.CharField(verbose_name='Ubicación', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Planilla'
        verbose_name_plural = 'Planillas'

    def save(self, *args, **kwargs):
        super(ListPeople, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.id_list)


class Person(MPTTModel):
    campaign = models.ForeignKey(Campaign, verbose_name='Campaña o candidatura',
                                 null=True, blank=True, on_delete=models.CASCADE)
    list_people = models.ManyToManyField(ListPeople, verbose_name='Planillas', through='Surveyed', blank=True)
    first_name = models.CharField(max_length=180, verbose_name='Nombres', null=True, blank=True)
    last_name = models.CharField(max_length=180, verbose_name='Apellidos', null=True, blank=True)
    sex = models.CharField(max_length=1, choices=strings.SEX_CHOICES, verbose_name='Sexo', null=True, blank=True)
    year_old = models.PositiveIntegerField(verbose_name='Edad', null=True, blank=True)
    identification_card = models.CharField(max_length=15, verbose_name='Cédula', blank=False, null=False)
    cellphone = models.CharField(max_length=10, verbose_name='Celular', null=True, blank=True)
    email = models.EmailField(max_length=100, verbose_name='Correo electrónico', null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name='País', on_delete=models.CASCADE)
    state = ChainedForeignKey(Region, verbose_name='Departamento',
                              chained_field='country', chained_model_field='country',
                              show_all=False, auto_choose=True)
    city = ChainedForeignKey(City, verbose_name='Municipio', chained_field='state', chained_model_field='state')
    zone = ChainedForeignKey(Zone, verbose_name='Zona', chained_field='city', null=True, blank=True, chained_model_field='city')
    sector = ChainedForeignKey(Neighborhood, verbose_name='Sector o barrio', chained_field='zone', null=True, blank=True,
                               chained_model_field='zone')
    address = models.CharField(max_length=180, verbose_name='Dirección')
    voting_post = models.ForeignKey(VotingPost, verbose_name='Puesto de votación', null=True, blank=True, on_delete=models.PROTECT)
    is_voter = models.BooleanField(verbose_name='¿Es votante?', default=False)
    campaign_charge = models.ForeignKey(CampaignCharge, verbose_name='Cargo en la campaña', null=True, blank=True, on_delete=models.PROTECT)
    order = models.PositiveIntegerField(verbose_name='Orden', default=0, blank=False, null=False)
    parent = TreeForeignKey('self', verbose_name='Persona a cargo', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    class MPTTMeta:
        order_insertion_by = ['order']

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)
        Person.objects.rebuild()

    def __str__(self):
        return '{} | {} {}'.format(self.identification_card, self.first_name, self.last_name)


class Surveyed(models.Model):
    campaign = models.ForeignKey(Campaign, verbose_name='Campaña o candidatura',
                                 null=True, blank=True, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, verbose_name='Persona', on_delete=models.CASCADE)
    list_people = models.ForeignKey(ListPeople, verbose_name='Planilla', on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, verbose_name='Actividad', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Encuestado'
        verbose_name_plural = 'Encuestados'

    def save(self, *args, **kwargs):
        super(Surveyed, self).save(*args, **kwargs)

    def __str__(self):
        return '{} | {}'.format(self.person, self.list_people)
