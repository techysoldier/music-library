# Generated by Django 4.0.4 on 2022-04-25 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('album', models.DecimalField(decimal_places=2, max_digits=8)),
                ('release_date', models.DateField()),
                ('genre', models.CharField(max_length=255)),
            ],
        ),
    ]
