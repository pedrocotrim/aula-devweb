# Generated by Django 2.2.5 on 2019-12-09 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0005_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carro',
            name='vendedor',
        ),
        migrations.AddField(
            model_name='carro',
            name='marca',
            field=models.CharField(default='Honda', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carro',
            name='quilometragem',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Vendedor',
        ),
    ]