# Generated by Django 4.0.4 on 2022-05-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento_artistico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicos',
            name='cuil',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='productores',
            name='cuil',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tecnicos',
            name='cuil',
            field=models.IntegerField(),
        ),
    ]