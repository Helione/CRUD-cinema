from django.db import models


class Animacao(models.Model):
      filme = models.CharField(max_length=60)
      nota = models.PositiveSmallIntegerField()
      imagem = models.ImageField(upload_to='midia', null=True, blank=True)

      def __str__(self):
        return self.filme

      class Meta:
        verbose_name_plural = 'Animações'


class Terror(models.Model):
      filme = models.CharField(max_length=60)
      nota = models.PositiveSmallIntegerField()
      imagem = models.ImageField(upload_to='midia', null=True, blank=True)

      def __str__(self):
        return self.filme

      class Meta:
        verbose_name_plural ='Terror'


class Comedia(models.Model):
      filme = models.CharField(max_length=60)
      nota = models.PositiveSmallIntegerField()
      imagem = models.ImageField(upload_to='midia', null=True, blank=True)

      class Meta:
        verbose_name_plural = 'Comédias'

      def __str__(self):
            return self.filme