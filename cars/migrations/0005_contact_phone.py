# Generated by Django 3.0.7 on 2020-09-02 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
