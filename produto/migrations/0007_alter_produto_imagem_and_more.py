# Generated by Django 5.0.4 on 2024-05-17 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0006_alter_produto_preco_marketing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produto_imagens/%Y/%m/'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(default=0, verbose_name='Preço Promo.'),
        ),
        migrations.AlterField(
            model_name='variacao',
            name='nome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]