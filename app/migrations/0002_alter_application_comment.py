# Generated by Django 4.2.2 on 2023-06-09 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='Comment',
            field=models.TextField(null=True),
        ),
    ]