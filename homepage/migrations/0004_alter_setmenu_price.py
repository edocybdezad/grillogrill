# Generated by Django 3.2.7 on 2021-10-05 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setmenu',
            name='price',
            field=models.CharField(max_length=8),
        ),
    ]
