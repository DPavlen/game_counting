# Generated by Django 3.2.16 on 2023-06-25 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0010_auto_20230625_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='идентификатор оплаты'),
        ),
    ]
