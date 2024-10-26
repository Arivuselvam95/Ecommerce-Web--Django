# Generated by Django 5.0.1 on 2024-02-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_com1', '0006_product_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(blank=True, choices=[('Fruit', 'Fruit'), ('Vegetable', 'Vegetable'), ('Meat', 'Meat'), ('Bread', 'Bread')], max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
