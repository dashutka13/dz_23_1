# Generated by Django 4.2.10 on 2024-03-18 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_remove_product_user_product_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]
