# Generated by Django 5.0 on 2023-12-21 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0014_orderitem_user_alter_orderitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='information',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
    ]
