# Generated by Django 2.2.5 on 2019-10-14 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0004_remove_imagem_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('pagina', models.CharField(max_length=50)),
            ],
        ),
    ]