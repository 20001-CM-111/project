# Generated by Django 4.1.1 on 2022-09-19 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0009_delete_add_to_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_To_Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductId', models.CharField(max_length=200)),
                ('Price', models.IntegerField()),
                ('Quantity', models.IntegerField()),
            ],
        ),
    ]