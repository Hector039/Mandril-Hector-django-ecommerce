# Generated by Django 5.1.1 on 2024-10-10 01:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_alter_cart_quantity'),
        ('products', '0002_alter_product_price_alter_product_stock'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='cart',
            name='owner_constraint',
        ),
        migrations.AddConstraint(
            model_name='cart',
            constraint=models.CheckConstraint(condition=models.Q(('userId', models.F('productId')), _negated=True), name='owner_constraint'),
        ),
    ]
