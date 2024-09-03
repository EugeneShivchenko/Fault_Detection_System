from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
import os

# Создавайте свои модели здесь.
class Engine(models.Model):
    """
    Модель для представления авиадвигателя.
    
    Поля:
        engine_name (CharField): хранит название авиадвигателя.
        serial_id (CharField): хранит серийный номер авиадвигателя.
        tail_number (CharField): хранит бортовой номер ВС.
    """
    engine_name = models.CharField(max_length=50,
                                   verbose_name='Название двигателя')
    serial_id = models.CharField(primary_key=True,
                                 max_length=50,
                                 verbose_name='Серийный номер двигателя')
    tail_number = models.CharField(max_length=20,
                                   verbose_name='Бортовой номер ВС')
    
    class Meta:
        """
        Содержит метаданные, которые определяют поведение модели.

        Атрибуты:
            verbose_name (str): человекочитаемое название модели.
            verbose_name_plural (str): множественное человекочитаемое название модели.
        """
        verbose_name = 'двигатель'
        verbose_name_plural = 'двигатели'
    
    def __str__(self):
        """Определяет, с каким именем объект будет отображаться в панели администрирования."""
        return str(self.serial_id)
    
class Report(models.Model):
    """
    Модель для представления отчета.
    
    Поля:
        report_id (BigAutoField): хранит ID отчета.
        user (ForeignKey): хранит ID пользователя.
        serial (ForeignKey): хранит серийный номер авиадвигателя.
        formation_date (DateTimeField): хранит дату и время формирования отчета.
        image_location (CharField): хранит путь расположения аннотированного изображения.
        defect (CharField): хранит перечень обнаруженных дефектов.
        defect_localization (CharField): хранит локализацию дефектов.
    """
    report_id = models.BigAutoField(primary_key=True,
                                    auto_created=True,
                                    verbose_name='ID отчета')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT,
                             verbose_name='ID пользователя')
    serial = models.ForeignKey(Engine,
                               on_delete=models.CASCADE,
                               verbose_name='Серийный номер двигателя')
    formation_date = models.DateTimeField(auto_now_add=True,
                                          verbose_name='Дата и время формирования')
    image_location = models.CharField(max_length=150,
                                      verbose_name='Расположение отчетного снимка')
    defect = models.CharField(max_length=175,
                              verbose_name='Обнаруженные дефекты')
    defect_localization = models.CharField(max_length=175,
                                           verbose_name='Локализация дефектов')

    class Meta:
        """
        Содержит метаданные, которые определяют поведение модели.

        Атрибуты:
            verbose_name (str): человекочитаемое название модели.
            verbose_name_plural (str): множественное человекочитаемое название модели.
        """
        verbose_name = 'отчет'
        verbose_name_plural = 'отчеты'

    def delete(self):
        """
        Позволяет автоматически удалять из файловой системы
        аннотированное изображение при удалении бъекта в панели администрирования.
        """
        base_path = os.getcwd()
        path = os.path.join(base_path, 'media', self.image_location)
        os.remove(path)
        super().delete()

    def __str__(self):
        """Определяет, с каким именем объект будет отображаться в панели администрирования."""
        return str('Отчет № ' + str(self.report_id))
    
class Original_image(models.Model):
    """
    Модель для представления оригинальных изображений.
    
    Поля:
        original_image_location (ImageField): хранит путь расположения изображения.
    """
    original_image_location = models.ImageField(upload_to='original_images/',
                                                verbose_name='Расположение оригинального снимка',
                                                validators=[FileExtensionValidator(['png'])])
    
    class Meta:
        """
        Содержит метаданные, которые определяют поведение модели.

        Атрибуты:
            verbose_name (str): человекочитаемое название модели.
            verbose_name_plural (str): множественное человекочитаемое название модели.
        """
        verbose_name = 'оригинальный снимок'
        verbose_name_plural = 'оригинальные снимки'
    
    def __str__(self):
        """Определяет, с каким именем объект будет отображаться в панели администрирования."""
        return str(os.path.basename(str(self.original_image_location)))