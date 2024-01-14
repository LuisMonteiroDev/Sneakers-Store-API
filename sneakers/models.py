from django.db import models
from django.contrib.postgres.fields import ArrayField


class Brands(models.Model):
    owners = models.ManyToManyField('users.UserProfile', verbose_name='Donos/Sócios', related_name='users_owners')
    brand_name = models.CharField('Nome da Marca', max_length=120)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


class Lines(models.Model):
    brand_line = models.ForeignKey(Brands, verbose_name='Linha da Marca', related_name='brand_line', on_delete=models.CASCADE)
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
    brand = models.ForeignKey(Brands, verbose_name='Marca', default='', related_name='sneaker_brand', on_delete=models.CASCADE)
    line = models.ForeignKey(Lines, verbose_name='Pertence a linha', blank=True, null=True, related_name='sneaker_line', on_delete=models.CASCADE)
    model = models.CharField('Modelo', max_length=55)
    in_stock = models.BooleanField('Em Estoque', default=True)
    available_sizes = ArrayField(models.FloatField(max_length=4), verbose_name='Tamanhos Disponiveis', default=list)

    def __str__(self):
        return f"{self.name} - {self.brand}"

    class Meta:
        verbose_name = 'Tênis'
        verbose_name_plural = 'Tênis'


class Adverts(models.Model):
    sneaker = models.ForeignKey(Sneakers, verbose_name='Tênis presente no anúncio', related_name='sneaker_advert', on_delete=models.CASCADE)
    advert = models.ImageField('Anúncio')
    create_at = models.DateTimeField('Criado em', help_text='OBS: A DATA DE CRIAÇÃO SERVE PARA INDICAR A PARTIR DE QUAL DATA O ANÙNCIO ESTARÁ VALENDO')
    expiration = models.DateTimeField('Expira em')

    def __str__(self):
        return self.sneaker.name

    class Meta:
        verbose_name = 'Anúncio'
        verbose_name_plural = 'Anúncios'
