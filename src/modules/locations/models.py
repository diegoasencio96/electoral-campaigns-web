from django.db import models

# Create your models here.


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    number_code = models.CharField(verbose_name='ISO 3166-1 numerico', max_length=3)
    alfa_two = models.CharField(verbose_name='ISO 3166-1 alfa-2', max_length=2)
    alfa_three = models.CharField(verbose_name='ISO 3166-1 alfa-3', max_length=3)
    name = models.CharField(verbose_name='Nombre del país', max_length=254)
    phone_code = models.CharField(verbose_name='Código número telefónico', max_length=5)
    icon = models.ImageField(verbose_name='Icono del país', upload_to='country_icon/')

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(verbose_name='Nombre del departamento', max_length=254)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='País')

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return '{}-{}'.format(self.country.name, self.name)


class City(models.Model):
    name = models.CharField(verbose_name='Nombre municipio', max_length=254)
    state = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name='Departamento')

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return '{}-{}-{}'.format(self.state.country.name, self.state.name, self.name)

    def save(self, *args, **kwargs):
        super(City, self).save(*args, **kwargs)


class Zone(models.Model):
    name = models.CharField(verbose_name='Zona', max_length=254)
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Municipio')

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'

    def __str__(self):
        return '{}-{}-{}-{}'.format(self.city.state.country.name, self.city.state.name, self.city.name, self.name)


class Neighborhood(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=254)
    zone_type = models.ForeignKey(Zone, on_delete=models.PROTECT, verbose_name='Zona')

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'

    def __str__(self):
        return '{}-{}-{}-{}-{}'.format(self.zone_type.city.state.country.name, self.zone_type.city.state.name,
                                               self.zone_type.city.name, self.zone_type.name, self.name)


class VotingPost(models.Model):
    name = models.CharField(verbose_name='Puesto de votación', max_length=254)
    sector = models.ForeignKey(Neighborhood, on_delete=models.PROTECT, verbose_name='Sector')

    class Meta:
        verbose_name = 'Puesto de votación'
        verbose_name_plural = 'Puestos de votaciones'

    def __str__(self):
        return '{}-{}-{}-{}-{}-{}'.format(self.sector.zone_type.city.state.country.name, self.sector.zone_type.city.state.name,
                                               self.sector.zone_type.city.name, self.sector.zone_type.name, self.sector.name, self.name)

