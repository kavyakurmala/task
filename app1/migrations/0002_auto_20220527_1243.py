# Generated by Django 3.2.5 on 2022-05-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwareRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testing', models.CharField(max_length=30)),
                ('developing', models.CharField(max_length=30)),
                ('sales', models.CharField(max_length=20)),
                ('maintaining', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='MakeupItems',
        ),
    ]