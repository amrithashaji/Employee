# Generated by Django 2.2 on 2019-10-18 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=255)),
                ('image_as_a_blob', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('email', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]
