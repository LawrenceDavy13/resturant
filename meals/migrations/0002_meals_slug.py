# Generated by Django 2.2.4 on 2019-08-19 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]