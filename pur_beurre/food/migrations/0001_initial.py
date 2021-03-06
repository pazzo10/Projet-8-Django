# Generated by Django 2.2 on 2019-05-10 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nutriscore', models.CharField(max_length=1)),
                ('url', models.URLField(max_length=250)),
                ('url_picture', models.URLField(max_length=250)),
                ('fat_100g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('saturated_fat_100g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sugars_100g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('salt_100g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fat_level', models.CharField(max_length=10)),
                ('salt_level', models.CharField(max_length=10)),
                ('saturated_fat_level', models.CharField(max_length=10)),
                ('sugars_level', models.CharField(max_length=10)),
                ('last_modified', models.DateField()),
                ('openff_id', models.BigIntegerField()),
                ('categories', models.ManyToManyField(to='food.Categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_foods', models.ManyToManyField(to='food.Food')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
