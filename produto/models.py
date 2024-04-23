from django.db import models
from PIL import Image
import os
from django.conf import settings
from django.utils.text import slugify

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to='produtos_imagens/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank = True, null = True)
    preco_marketing = models.FloatField(verbose_name='Preço')
    preco_marketing_promocional = models.FloatField(default=0, verbose_name='Preço Promocional')
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=((
            'V', 'Variável'),
            ('S', 'Simples'),
        )
    )

    def get_preco_formatado(self):
        return f'R$ {self.preco_marketing:.2f}'.replace('.', ',')
    get_preco_formatado.short_description = 'Preço'

    def get_precopromocional_formatado(self):
        return f'R$ {self.preco_marketing_promocional}'.replace('.', ',')
    get_precopromocional_formatado.short_description = 'Preço Promocional'

    @staticmethod
    def resize_image(img, new_widht = 800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_widht, original_height = img_pil.size

        if original_widht <= new_widht:
            print("retornando, largura original maior que nova largura!")
            img_pil.close()
            return

        new_height = round((new_widht * original_height) / original_widht)

        new_img = img_pil.resize((new_widht, new_height), Image.LANCZOS)
        new_img.save(img_full_path, optimize = True, quality = 50)
        
        print(img.name)

    def save(self, *args, **kwargs):

        if not self.slug:
             slug = f'{slugify(self.nome)}'
             self.slug = slug

        super().save(*args, **kwargs)

        max_image = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image)

    def __str__(self):
        return self.nome

class Variacao(models.Model):
        produto = models.ForeignKey(Produto, on_delete = models.CASCADE)
        nome = models.CharField(max_length= 50)
        preco = models.FloatField()
        preco_promocional = models.FloatField(default=0)
        estoque = models.PositiveIntegerField(default=1)

        def __str__(self):
            return self.nome or self.produto.nome
        
        class Meta:
             verbose_name = "Variação"
             verbose_name_plural = "Variações"