# Generated by Django 4.2.10 on 2024-02-25 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('nivel', models.CharField(choices=[('Iniciante', 'Iniciante'), ('Intermediário', 'Intermediário'), ('Avançado', 'Avançado')], max_length=50)),
                ('carga_horaria', models.IntegerField()),
                ('data_do_curso', models.DateField(help_text='aaaa/mm/dd')),
                ('descricao', models.TextField()),
            ],
            options={
                'verbose_name': 'Cadastro de curso',
                'verbose_name_plural': 'Cadastros de cursos',
                'ordering': ['-data_do_curso'],
            },
        ),
    ]