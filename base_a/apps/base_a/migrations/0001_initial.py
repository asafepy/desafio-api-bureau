# Generated by Django 2.1 on 2018-11-19 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Divida',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),

                ('company', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('contract', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('cpf', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='divida',
            name='pessoa',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='dividas',
                to='base_a.Pessoa'),
        ),
    ]
