# Generated by Django 4.0.3 on 2023-11-08 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='productos')),
                ('descripcion', models.CharField(max_length=255)),
                ('precio', models.IntegerField()),
                ('active', models.BooleanField(default=False)),
                ('observacion', models.CharField(blank=True, max_length=255, null=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categorias.categoria')),
            ],
        ),
    ]
