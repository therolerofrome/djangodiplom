# Generated by Django 3.2.13 on 2022-06-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayly', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
