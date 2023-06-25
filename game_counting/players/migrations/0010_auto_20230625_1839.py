# Generated by Django 3.2.16 on 2023-06-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0009_auto_20230625_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='game',
            field=models.ManyToManyField(related_name='games', to='players.Game', verbose_name='URL игры'),
        ),
        migrations.AlterField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(related_name='players', to='players.Player', verbose_name='Основное имя игрока'),
        ),
    ]