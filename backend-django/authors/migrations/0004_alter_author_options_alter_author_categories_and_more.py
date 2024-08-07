# Generated by Django 5.0.4 on 2024-06-15 12:18

import utils.custom_upload_path
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_authorcategory_authortag_remove_author_main_genre_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('name',), 'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterField(
            model_name='author',
            name='categories',
            field=models.ManyToManyField(blank=True, to='authors.authorcategory'),
        ),
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(default='authors/photos/default.jpg', upload_to=utils.custom_upload_path.CustomUploadPath('books/covers')),
        ),
        migrations.AlterField(
            model_name='author',
            name='tags',
            field=models.ManyToManyField(blank=True, to='authors.authortag'),
        ),
    ]
