# Generated by Django 4.1.1 on 2022-09-17 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MyApp', '0004_delete_createaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.TextField(max_length=150)),
                ('Password', models.CharField(max_length=8)),
                ('ConfirmPassword', models.CharField(max_length=8)),
                ('MobileNo', models.IntegerField()),
            ],
        ),
    ]
