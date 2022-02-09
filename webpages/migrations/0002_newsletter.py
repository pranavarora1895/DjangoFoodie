# Generated by Django 4.0.1 on 2022-02-09 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]