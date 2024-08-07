# Generated by Django 5.0.4 on 2024-06-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_alter_author_options_author_birth_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AuthorTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='author',
            name='main_genre',
        ),
        migrations.AddField(
            model_name='author',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='authors.authorcategory'),
        ),
        migrations.AddField(
            model_name='author',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='authors.authortag'),
        ),
    ]
