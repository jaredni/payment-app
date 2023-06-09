# Generated by Django 4.2 on 2023-04-20 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='payment',
            name='paid_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='code',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='payment',
            name='reference_code',
            field=models.CharField(max_length=45, unique=True),
        ),
    ]
