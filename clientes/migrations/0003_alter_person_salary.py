# Generated by Django 3.2.7 on 2021-09-02 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_person_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='salary',
            field=models.DecimalField(decimal_places=4, max_digits=7),
        ),
    ]
