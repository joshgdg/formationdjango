from django.db import models
from django.utils.translation import activate


# Create your models here.
class Etudiant(models.Model):
    nom = models.CharField(max_length=255,
                           verbose_name='Nom',
                           null=False, blank=False)

    prenoms = models.CharField(max_length=255,
                               verbose_name='Prénoms',
                               null=False, blank=False)

    contact = models.CharField(max_length=16,
                               verbose_name='Contact',
                               null=False, blank=True)

    class Meta:
        db_table = "core_etudiant"
        verbose_name = 'Étudiant'
        verbose_name_plural = 'Étudiants'

    def __str__(self):
        return self.prenoms + ' ' + self.nom
