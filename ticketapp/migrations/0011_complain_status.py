# Generated by Django 3.0.3 on 2020-02-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0010_conversation_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
