# Generated by Django 5.0.6 on 2024-06-03 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('count_views', models.PositiveIntegerField()),
                ('position', models.PositiveIntegerField()),
            ],
        ),
    ]
