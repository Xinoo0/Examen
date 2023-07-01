# Generated by Django 4.2.2 on 2023-07-01 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebTaller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('stock', models.PositiveSmallIntegerField()),
            ],
        ),
    ]