# Generated by Django 4.0.4 on 2022-05-14 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempedido',
            name='preco',
            field=models.FloatField(verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='preco_promocional',
            field=models.FloatField(default=0, verbose_name='Preço promocional'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='variacao',
            field=models.CharField(max_length=255, verbose_name='Variação'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='variacao_id',
            field=models.PositiveIntegerField(verbose_name='Variação ID'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]