# Generated by Django 4.2.2 on 2023-07-09 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='upadte',
            new_name='update',
        ),
    ]