# Generated by Django 5.1 on 2024-08-13 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('matricula', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('carga_horaria', models.IntegerField()),
                ('descricao', models.TextField()),
                ('alunos', models.ManyToManyField(to='suap.aluno')),
            ],
        ),
    ]
