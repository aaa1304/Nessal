# Generated by Django 4.2.1 on 2023-05-17 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=15, null=True)),
                ('service', models.CharField(blank=True, choices=[('creat web', 'creat web'), ('online ads', 'online ads')], max_length=15, null=True)),
                ('text', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
