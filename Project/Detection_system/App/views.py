from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import OriginalImageForm, ReportForm
from ultralytics import YOLO
from PIL import Image
from io import BytesIO
import numpy as np
import base64
import cv2
import os

# Создавайте свои представления здесь.

# Перечень цветов в формате RGB для классов дефектов.
COLORS = [(255, 0, 0),
          (0, 0, 255),
          (255, 255, 0),
          (0, 255, 0)]

def home(request):
    """
    Принимает объект HttpRequest. Если пользователь авторизован, то перенаправляет в личный кабинет.
    Иначе выводит главную страницу.
    """
    if request.user.is_authenticated:
        return redirect('account')
    else:
        return render(request, 'home.html')

@login_required
def account(request):
    """Принимает объект HttpRequest. Выводит личный кабинет."""
    return render(request, 'account_base.html')

@login_required
def upload_image(request):
    """Принимает объект HttpRequest. Позволяет через форму загружать в систему изображения."""
    if request.method == 'POST':
        form = OriginalImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            original_image_name = form.cleaned_data['original_image_location'].name
            base_path = os.getcwd()
            original_image_path = os.path.join(base_path, 'media', 'original_images', original_image_name)
            image = Image.open(original_image_path)
            buff = BytesIO()
            image.save(buff, format='PNG')
            image_string = base64.b64encode(buff.getvalue()).decode('utf-8')
            notification = f'Изображение {original_image_name} загружено успешно!'
            notification_message = {'image_string': image_string, 'notification': notification}
            request.session['original_image_path'] = original_image_path
            request.session['detection_not_completed'] = True
            return render(request, 'upload_notification.html', context=notification_message)
    else:
        form = OriginalImageForm()
    return render(request, 'image_form.html', {'form': form})

@login_required
def start_detection(request):
    """
    Принимает объект HttpRequest. Загружает модель YOLOv8s,
    делает прогноз по изображению, сохраняет аннотированное изображение.
    """
    try:
        class_list = []
        base_path = os.getcwd()
        model_path = os.path.join(base_path, 'App', 'static', 'model', 'best.pt')
        model = YOLO(model_path)
        original_image = cv2.imread(request.session['original_image_path'])
        result = model.predict(source=original_image,
                               show_conf=False,
                               save=False,
                               imgsz=640,
                               conf=0.5,
                               verbose=False)[0]
        img = result.orig_img
        classes_names = result.names
        classes = result.boxes.cls.cpu().numpy()
        boxes = result.boxes.xyxy.cpu().numpy().astype(np.int32)
        grouped_objects = {}
        for class_id, box in zip(classes, boxes):
            class_name = classes_names[int(class_id)]
            color = COLORS[int(class_id) % len(COLORS)]
            if class_name not in grouped_objects:
                grouped_objects[class_name] = []
            grouped_objects[class_name].append(box)
            x1, y1, x2, y2 = box
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 4)
            cv2.putText(img, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, color, 3)
        reporting_image_name = os.path.basename(request.session['original_image_path'])
        reporting_image_path = os.path.join(base_path, 'media', 'reporting_images', reporting_image_name)
        cv2.imwrite(reporting_image_path, img)
        for cls in np.unique(result.boxes.cls):
            class_list.append(model.names[int(cls)])
        image = Image.open(reporting_image_path)
        buff = BytesIO()
        image.save(buff, format='PNG')
        image_string = base64.b64encode(buff.getvalue()).decode('utf-8')
        count_of_classes = len(class_list)
        notification_message = {'image_string': image_string,
                                'count_of_classes': count_of_classes,
                                'class_list': class_list}
        request.session['reporting_image_name'] = reporting_image_name
        request.session['class_list'] = class_list
        request.session['detection_not_completed'] = False
        return render(request, 'detection_notification.html', context=notification_message)
    except Exception:
        notification = 'Пожалуйста, загрузите изображение.'
        notification_message = {'notification': notification}
        return render(request, 'notification.html', context=notification_message)

@login_required
def save_report(request):
    """Принимает объект HttpRequest. Позволяет через форму сохранять в системе отчет."""
    try:
        if request.session['detection_not_completed']:
            notification = 'Пожалуйста, выполните детектирование.'
            notification_message = {'notification': notification}
            return render(request, 'notification.html', context=notification_message)
        else:
            if request.method == 'POST':
                form = ReportForm(request.POST)
                if form.is_valid():
                    form.save()
                    notification = f"Отчет о выполненном детектировании сохранен успешно!"
                    notification_message = {'notification': notification}
                    return render(request, 'notification.html', context=notification_message)
            else:
                image_location = 'reporting_images/' + request.session['reporting_image_name']
                defect = ', '.join(request.session['class_list'])
                data = {'user': request.user.id,
                        'image_location': image_location,
                        'defect': defect}
                form = ReportForm(data)
            return render(request, 'report_form.html', {'form': form})
    except Exception:
        notification = 'Пожалуйста, выполните детектирование.'
        notification_message = {'notification': notification}
        return render(request, 'notification.html', context=notification_message)