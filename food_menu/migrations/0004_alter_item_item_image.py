# Generated by Django 5.1.4 on 2025-03-20 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_menu', '0003_item_item_image_alter_item_item_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png', max_length=500),
        ),
    ]
