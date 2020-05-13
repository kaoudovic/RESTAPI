# Generated by Django 3.0.6 on 2020-05-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('date_re', models.DateField()),
                ('department', models.CharField(max_length=10)),
            ],
        ),
    ]
