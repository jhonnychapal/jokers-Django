# Generated by Django 2.2.1 on 2019-06-22 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jokersapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle',
            name='factura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='jokersapp.Factura'),
        ),
    ]