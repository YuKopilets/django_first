# Generated by Django 3.1 on 2020-08-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_text', models.TextField(verbose_name='entry_text')),
                ('entry_date', models.DateTimeField(verbose_name='entry_date')),
            ],
        ),
    ]
