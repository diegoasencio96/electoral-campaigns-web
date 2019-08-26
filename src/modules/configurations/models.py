from django.db import models
# Create your models here.


class PoliticalParty(models.Model):
    name = models.CharField(max_length=180, verbose_name='Nombre del partido')
    icon = models.ImageField(verbose_name='Logo del partido', upload_to='political_party_icon/')

    class Meta:
        verbose_name = 'Partido político'
        verbose_name_plural = 'Partidos políticos'

    def save(self, *args, **kwargs):
        super(PoliticalParty, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)

