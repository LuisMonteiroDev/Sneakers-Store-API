from django.db import models
from django.contrib.postgres.fields import ArrayField


class Brands(models.Model):
    brand_name = models.CharField('Nome da Marca', max_length=120)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


class Lines(models.Model):
    create_line = models.CharField('Criar Linha', max_length=50)

    def __str__(self):
        return self.create_line

    class Meta:
        verbose_name = 'Linha de Tênis'
        verbose_name_plural = 'Linhas de Tênis'


class Sneakers(models.Model):
    photo = models.ImageField('Foto')
    name = models.CharField('Nome', max_length=255)
    price = models.FloatField('Preço')
    brand = models.ForeignKey(Brands, verbose_name='Marca', default='', on_delete=models.CASCADE)
    line = models.ForeignKey(Lines, verbose_name='Pertence a linha', blank=True, null=True, on_delete=models.CASCADE)
    model = models.CharField('Modelo', max_length=55)
    available_sizes = ArrayField(models.FloatField(max_length=4), verbose_name='Tamanhos Disponiveis', default=list)

    def __str__(self):
        return f"{self.name} - {self.brand}"

    class Meta:
        verbose_name = 'Tênis'
        verbose_name_plural = 'Tênis'


