# Generated by Django 3.2 on 2021-05-01 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(max_length=200)),
                ('last_request', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gpio', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.board')),
            ],
        ),
    ]