# Generated by Django 4.1 on 2022-10-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_accountsdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsdata',
            name='account_no',
            field=models.IntegerField(),
        ),
    ]
