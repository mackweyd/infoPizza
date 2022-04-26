# Generated by Django 4.0.4 on 2022-04-25 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=250)),
                ('p1', models.DecimalField(decimal_places=2, max_digits=4)),
                ('p2', models.DecimalField(decimal_places=2, max_digits=4)),
                ('p3', models.DecimalField(decimal_places=2, max_digits=4)),
                ('p4', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'db_table': 'item',
            },
        ),
    ]
