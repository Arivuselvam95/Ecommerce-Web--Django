# Generated by Django 5.0.1 on 2024-02-20 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_com1', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form1',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
