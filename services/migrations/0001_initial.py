# Generated by Django 5.0.6 on 2024-07-29 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.CharField(max_length=50)),
                ('service_title', models.CharField(max_length=100)),
                ('service_description', models.TextField()),
            ],
        ),
    ]