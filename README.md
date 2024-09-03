# Система детектирования повреждений лопаток компрессора авиационных двигателей
## Описание задачи
На сегодняшний день многие авиакомпании используют машинное обучение, в частности компьютерное зрение, в рамках предсказательного технического обслуживания и ремонта. Это повышает эффективность эксплуатации воздушных судов, сводя к минимуму время их простоя из-за внепланового ремонта, а также снижает уровень расходов на обслуживание.

Поставленная мной задача заключалась в разработке специальной системы, позволяющей проводить дефектоскопию в автоматизированном режиме путем нахождения дефектов на фотографиях рабочих лопаток авиадвигателя.
## Описание продукта, который решает задачу
Данная система представляет собой веб-приложение. Бэкенд написан на языке Python с использованием фреймворка Django. Фронтенд написан с помощью HTML, CSS и фреймворка Bootstrap. Для реализации базы данных использовался MySQL Server. Для детектирования применяется нейронная сеть YOLOv8s. Пользователь системы имеет личный кабинет, через который может:
- загружать изображения;
- выполнять детектирование;
- формировать отчеты и сохранять их.

Также имеется панель администратора, через которую можно управлять таблицами базы данных. Всего есть 5 таблиц для хранения информации о пользователях, группах, двигателях, изображениях и отчетах.
## Установка (Windows)
1. Клонирование репозитория

```git clone https://github.com/EugeneShivchenko/Fault_Detection_System.git```

2. Переход в директорию Project

```cd Project```

3. Создание виртуального окружения

```python -m venv .venv```

4. Активация виртуального окружения

```.venv\Scripts\activate.bat```

5. Установка зависимостей

```pip install -r requirements.txt```

6. Переход в директорию Detection_system

```cd Detection_system```

7. Запуск веб-приложения

```python manage.py runserver```

## Установка MySQL (Windows)
Подробная инструкция по установке MySQL на компьютер с ОС Windows доступна по ссылке: <https://timeweb.cloud/tutorials/mysql/kak-ustanovit-mysql-na-windows>

После успешной установки MySQL на компьютер, выполните следующие действия
1. Переход в директорию Detection_system

```cd Detection_system```

2. Применение миграций

```python manage.py migrate```

## Необходимые данные и пайплайн ML экспериментов (распаковка данных, обучение, валидация и т. д.)
Исходный датасет, который применялся для формирования собственного набора данных, доступен по ссылке: <https://drive.google.com/file/d/14wkZAFFeudlg0NMFLsiGwS0E593b-lNo/view?usp=share_link>

[Набор данных](https://github.com/EugeneShivchenko/Fault_Detection_System/tree/b60fe56f07630d8cd6edc8b370fd8465ec63c22b/Required%20data%20and%20pipeline/Dataset)

[Веса нейронной сети](https://github.com/EugeneShivchenko/Fault_Detection_System/tree/b60fe56f07630d8cd6edc8b370fd8465ec63c22b/Required%20data%20and%20pipeline/Weights)

[Изображения для демонстрации работы системы](https://github.com/EugeneShivchenko/Fault_Detection_System/tree/b60fe56f07630d8cd6edc8b370fd8465ec63c22b/Required%20data%20and%20pipeline/Images%20to%20demonstrate%20the%20work)

[Графики](https://github.com/EugeneShivchenko/Fault_Detection_System/tree/b60fe56f07630d8cd6edc8b370fd8465ec63c22b/Required%20data%20and%20pipeline/Charts)

[Пайплайн ML экспериментов](https://github.com/EugeneShivchenko/Fault_Detection_System/tree/b60fe56f07630d8cd6edc8b370fd8465ec63c22b/Required%20data%20and%20pipeline/ML%20Experiment%20Pipeline)

## Документация
[Инструкция по работе в системе](https://github.com/EugeneShivchenko/Fault_Detection_System/tree/b60fe56f07630d8cd6edc8b370fd8465ec63c22b/Documentation)
