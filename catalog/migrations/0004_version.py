# Generated by Django 5.0.2 on 2024-02-24 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_blog_options_rename_title_blog_blog_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='номер версии')),
                ('name', models.CharField(max_length=50, verbose_name='название версии')),
                ('is_active', models.BooleanField(default=True, verbose_name='признак текущей версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
                'ordering': ('name',),
            },
        ),
    ]
