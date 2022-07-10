# Generated by Django 4.0.6 on 2022-07-10 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
                ('objetivo', models.CharField(max_length=200)),
                ('idade_minima', models.IntegerField(verbose_name='Idade Mínima')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('carga_horaria', models.IntegerField(verbose_name='Carga Horária')),
                ('ordem', models.IntegerField()),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.modulo')),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15)),
                ('upload', models.FileField(upload_to='uploads/')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.curso')),
            ],
        ),
    ]