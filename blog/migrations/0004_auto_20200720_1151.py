# Generated by Django 3.0.3 on 2020-07-20 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200720_1150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['published_date']},
        ),
    ]
