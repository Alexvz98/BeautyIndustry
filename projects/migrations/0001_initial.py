# Generated by Django 4.1.7 on 2023-04-18 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('text', models.TextField(verbose_name='Отзыв')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название тэга')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('featured_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='projects/%Y/%m/%d/', verbose_name='Изображение')),
                ('demo_link', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Ссылка(по необходимости')),
                ('source_link', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Ссылка(по необходимости)')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
                ('tags', models.ManyToManyField(blank=True, to='projects.tag', verbose_name='Тэги')),
            ],
        ),
    ]