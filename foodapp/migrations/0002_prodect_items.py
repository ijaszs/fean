# Generated by Django 4.2.3 on 2023-08-10 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='prodect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=200)),
                ('limit', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('title', models.CharField(max_length=255)),
                ('discription', models.TextField()),
                ('amound', models.CharField(max_length=50)),
                ('prodect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.prodect')),
            ],
        ),
    ]
