# Generated by Django 3.0.8 on 2020-08-10 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20200809_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcategory',
            name='item',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_list', to='auctions.Item'),
        ),
    ]
