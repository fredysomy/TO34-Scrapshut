# Generated by Django 3.0.8 on 2020-09-26 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0003_productquery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productquery',
            name='quantity_needed',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='productquery',
            name='reciever_phno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='donator_phno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='phno',
            field=models.IntegerField(),
        ),
    ]