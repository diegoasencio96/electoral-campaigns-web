from django.db import models
from ..campaigns.models import Campaign
from django.contrib.auth.models import AbstractUser
from ..locations.models import Country


class User(AbstractUser):
    identification_card = models.CharField(max_length=15, verbose_name='Cédula', blank=True, null=True)
    address = models.CharField(verbose_name='Dirección', max_length=30, null=True, blank=True)
    cellphone = models.CharField(verbose_name='Celular', max_length=15, null=True, blank=True)
    birth_date = models.DateField(verbose_name='Fecha de nacimiento', null=True, blank=True)
    campaign = models.ForeignKey(Campaign, verbose_name='Campaña o candidatura',
                                 null=True, blank=True, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, verbose_name='País', null=True, blank=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


