# Generated by Django 5.0.4 on 2024-05-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_author_delete_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(blank=True, to='books.category'),
        ),
    ]
