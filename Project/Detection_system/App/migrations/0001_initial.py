# Generated by Django 4.2 on 2024-08-09 11:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('engine_name', models.CharField(max_length=50, verbose_name='Название двигателя')),
                ('serial_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Серийный номер двигателя')),
                ('tail_number', models.CharField(max_length=20, verbose_name='Бортовой номер ВС')),
            ],
            options={
                'verbose_name': 'двигатель',
                'verbose_name_plural': 'двигатели',
            },
        ),
        migrations.CreateModel(
            name='Original_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_image_location', models.ImageField(upload_to='original_images/', validators=[django.core.validators.FileExtensionValidator(['png'])], verbose_name='Расположение оригинального снимка')),
            ],
            options={
                'verbose_name': 'оригинальный снимок',
                'verbose_name_plural': 'оригинальные снимки',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID отчета')),
                ('formation_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время формирования')),
                ('image_location', models.CharField(max_length=150, verbose_name='Расположение отчетного снимка')),
                ('defect', models.CharField(max_length=175, verbose_name='Обнаруженные дефекты')),
                ('defect_localization', models.CharField(max_length=175, verbose_name='Локализация дефектов')),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.engine', verbose_name='Серийный номер двигателя')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ID пользователя')),
            ],
            options={
                'verbose_name': 'отчет',
                'verbose_name_plural': 'отчеты',
            },
        ),
    ]
