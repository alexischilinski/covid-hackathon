# Generated by Django 3.0.4 on 2020-03-27 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidfitness', '0014_auto_20200327_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(blank=True)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('country', models.CharField(blank=True, max_length=200)),
                ('bio', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='challenge_photos')),
                ('age', models.IntegerField(blank=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
