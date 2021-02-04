# Generated by Django 3.1.2 on 2021-02-04 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0005_auto_20210204_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='oferta',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_producto',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_venta', models.DateTimeField(null=True)),
                ('oferta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='venta.oferta')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='venta.producto')),
                ('tienda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='venta.tienda')),
            ],
        ),
    ]
