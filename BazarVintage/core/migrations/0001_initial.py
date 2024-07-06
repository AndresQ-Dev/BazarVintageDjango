# Generated by Django 5.0.6 on 2024-07-05 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('idProduct', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('description', models.TextField(max_length=150)),
                ('image', models.ImageField(upload_to='media/products/')),
                ('category', models.CharField(choices=[('category1', 'Madera'), ('category2', 'Bazar'), ('category3', 'Deco')], max_length=100)),
            ],
        ),
    ]