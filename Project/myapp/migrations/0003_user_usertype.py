# Generated by Django 4.0.5 on 2022-06-29 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_contact_address_contact_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(default='patient', max_length=100),
        ),
    ]