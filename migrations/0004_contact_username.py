# Generated by Django 4.2.1 on 2023-05-18 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nessal_app', '0003_alter_contact_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]