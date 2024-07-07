# Generated by Django 5.0.6 on 2024-07-07 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Madera', 'Madera'), ('Bazar', 'Bazar'), ('Deco', 'Deco')], max_length=100, verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=150, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='products/default_image.jpg', null=True, upload_to='products/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(verbose_name='Stock'),
        ),
    ]
