# Generated by Django 4.2.13 on 2024-05-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_depositproduct_fin_co_subm_day_and_more'),
        ('accounts', '0003_subscribedsaving_subscribeddeposit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subscribed_deposits',
            field=models.ManyToManyField(related_name='subscribed_savings', through='accounts.SubscribedDeposit', to='products.depositoption'),
        ),
        migrations.AlterField(
            model_name='user',
            name='subscribed_savings',
            field=models.ManyToManyField(related_name='subscribed_deposits', through='accounts.SubscribedSaving', to='products.savingoption'),
        ),
    ]
