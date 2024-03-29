# Generated by Django 4.1.3 on 2023-01-02 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ultrasound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand', models.CharField(choices=[('GE Healthcare', 'GE Healthcare'), ('Samsung', 'Samsung'), ('Hitachi', 'Hitachi'), ('Philips', 'Philips'), ('Siemens', 'Siemens'), ('Toshiba', 'Toshiba'), ('Aloka', 'Aloka')], max_length=255)),
                ('Model', models.CharField(max_length=255)),
                ('Problem', models.CharField(max_length=255)),
                ('Reason', models.CharField(max_length=255)),
                ('Fix_problem', models.CharField(max_length=255)),
                ('Photo', models.ImageField(upload_to='photos/%y/%m/%d/')),
            ],
        ),
    ]
