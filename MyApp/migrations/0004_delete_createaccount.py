# Generated by Django 4.1.1 on 2022-09-17 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_createaccount_delete_article'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CreateAccount',
        ),
    ]