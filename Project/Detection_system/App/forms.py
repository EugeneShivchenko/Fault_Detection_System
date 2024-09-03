from django import forms
from .models import Original_image, Report

class OriginalImageForm(forms.ModelForm):
    """Класс для определения формы загрузки оригинальных изображений."""
    class Meta:
        """
        Содержит метаданные, используемые для настройки различных аспектов формы.

        Атрибуты:
            model: устанавливает связь формы с моделью Original_image.
            labels: устанавливает человекочитаемые названия полей в форме.
            fields: определяет поля для отображения в форме.
        """
        model = Original_image
        labels = {'original_image_location': ''}
        fields = ['original_image_location']

class ReportForm(forms.ModelForm):
    """Класс для определения формы сохранения отчета."""
    class Meta:
        """
        Содержит метаданные, используемые для настройки различных аспектов формы.

        Атрибуты:
            model: устанавливает связь формы с моделью Report.
            widgets: устанавливает классы виджетов, которые будут использоваться при рендеринге полей.
            fields: определяет поля для отображения в форме.
        """
        model = Report
        widgets = {'user': forms.HiddenInput(),
                   'image_location': forms.HiddenInput()}
        fields = ['user', 'serial', 'image_location', 'defect', 'defect_localization']