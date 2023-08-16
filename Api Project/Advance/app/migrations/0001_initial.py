# Generated by Django 4.2.2 on 2023-08-15 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flipkart_Api',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Price', models.IntegerField()),
                ('Description', models.TextField()),
                ('No_Of_Reviews_And_Ratings', models.IntegerField()),
                ('Ratings', models.IntegerField()),
                ('No_Of_Media_Counts_Present_Product_Box', models.IntegerField()),
            ],
        ),
    ]
