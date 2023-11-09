# Generated by Django 4.2.6 on 2023-10-06 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='acuerdo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fec_acu', models.DateTimeField()),
                ('des_acu', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='buscar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_gen', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_tip_pag', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_reseña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_tip_res', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_tip_usu', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_usu', models.TextField(max_length=30)),
                ('ape_usu', models.TextField(max_length=30)),
                ('corre_usu', models.TextField(max_length=50)),
                ('rut_usu', models.TextField(max_length=12)),
                ('num_usu', models.TextField(max_length=12)),
                ('des_usu', models.TextField(max_length=100)),
                ('est_prem', models.BooleanField(verbose_name=False)),
                ('fec_res', models.DateTimeField()),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.genero')),
                ('tipo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.tipo_usuario')),
            ],
        ),
        migrations.CreateModel(
            name='transferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mon', models.IntegerField()),
                ('fec_mon', models.DateTimeField()),
                ('acuerdo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.acuerdo')),
                ('tipo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.tipo_pago')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='reseña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des_res', models.TextField(max_length=50)),
                ('fec_res', models.DateTimeField()),
                ('tipo_reseña', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.tipo_reseña')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tit_pub', models.TextField(max_length=50)),
                ('fec_pub', models.DateTimeField()),
                ('des_pub', models.TextField(max_length=100)),
                ('buscar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.buscar')),
                ('reseña', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.reseña')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='contactar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con', models.TextField(max_length=50)),
                ('fec_con', models.DateTimeField()),
                ('buscar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.buscar')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='buscar',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.usuario'),
        ),
        migrations.AddField(
            model_name='acuerdo',
            name='contactar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.contactar'),
        ),
        migrations.AddField(
            model_name='acuerdo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.usuario'),
        ),
    ]