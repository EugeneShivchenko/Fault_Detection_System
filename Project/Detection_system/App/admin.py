from django.contrib import admin
from .models import Engine, Report, Original_image

class EngineAdmin(admin.ModelAdmin):
    """Класс для отключения редактирования объектов модели Engine в панели администрирования."""
    def get_readonly_fields(self, request, obj=None):
        """Получает поля, доступные только для чтения."""
        if obj:
            return self.readonly_fields + tuple([item.name for item in obj._meta.fields])
        return self.readonly_fields
    def change_view(self, request, object_id, form_url='', extra_context=None):
        """Изменяет интерфейс работы с объектами модели Engine в панели администрирования."""
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        extra_context['show_save_and_add_another'] = False
        return super(EngineAdmin, self).change_view(request, object_id, extra_context=extra_context)

class ReportAdmin(admin.ModelAdmin):
    """Класс для отключения редактирования объектов модели Report в панели администрирования."""
    def get_readonly_fields(self, request, obj=None):
        """Получает поля, доступные только для чтения."""
        if obj:
            return self.readonly_fields + tuple([item.name for item in obj._meta.fields])
        return self.readonly_fields
    def change_view(self, request, object_id, form_url='', extra_context=None):
        """Изменяет интерфейс работы с объектами модели Report в панели администрирования."""
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        extra_context['show_save_and_add_another'] = False
        return super(ReportAdmin, self).change_view(request, object_id, extra_context=extra_context)
    
class Original_imageAdmin(admin.ModelAdmin):
    """Класс для отключения редактирования объектов модели Original_image в панели администрирования."""
    def get_readonly_fields(self, request, obj=None):
        """Получает поля, доступные только для чтения."""
        if obj:
            return self.readonly_fields + tuple([item.name for item in obj._meta.fields])
        return self.readonly_fields
    def change_view(self, request, object_id, form_url='', extra_context=None):
        """Изменяет интерфейс работы с объектами модели Original_image в панели администрирования."""
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        extra_context['show_save_and_add_another'] = False
        return super(Original_imageAdmin, self).change_view(request, object_id, extra_context=extra_context)

# Зарегистрируйте свои модели здесь.
admin.site.register(Engine, EngineAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Original_image, Original_imageAdmin)