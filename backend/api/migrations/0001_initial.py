# Generated by Django 2.0.4 on 2018-04-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=40)),
                ('item_id', models.IntegerField()),
            ],
        ),
    ]
