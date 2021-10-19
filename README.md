# Blog sensive

Блог о коммерческом успехе вымышленного автора

## Описание

Посты с советами по бизнесу, жизни.

### Начало работы

- Необходимо:
  + создать [суперпользователя](https://github.com/Padking/blog-sensive#установка),
  + [наполнить](https://github.com/Padking/blog-sensive#установка) базу данных (БД).

### Особенности

- позволяет выбрать пост к прочтению из числа:
  * популярных по кол-ву лайков (см. [слайдер](https://github.com/Padking/blog-sensive#главная-страница) под баннером),
  * свежих по дате,
  * популярных по кол-ву тегов (см. [сайдбар](https://github.com/Padking/blog-sensive#главная-страница)).
- предоставляет [пост](https://github.com/Padking/blog-sensive#страница-поста) к прочтению,
- обеспечивает возможность:
  * создать/редактировать читателя/пост/комментарий/тег.

## Примеры использования

  Главная страница для выбора поста к прочтению:

  ![site_1_index_page](https://github.com/Padking/sensive-blog/blob/master/screenshots/site_1_index_page.gif)


  Страница поста:

  ![site_2_posts_page](https://github.com/Padking/sensive-blog/blob/master/screenshots/site_2_posts_page.gif)


## Предметная область

  Схема сущностей БД:

  ![db_scheme](https://github.com/Padking/sensive-blog/blob/master/screenshots/db_scheme.png)


## Структура проекта

### Главная страница

* блок 1 - слайдер с популярными постами
* блок 2 - часть страницы со свежими постами
* блок 3 - сайдбар с тегами постов

### Страница поста

* блок 1 - пост, комментарии, лайки
* блок 2 - сайдбар с тегами постов
* блок 3 - сайдбар с популярными постами

### Страница тега

* блок 1 - список постов, связанных с тегом
* блок 2 - сайдбар с тегами постов
* блок 3 - сайдбар с популярными постами

## Требования к окружению

* Python 3.7 и выше,
* Linux/Windows,
* Переменные окружения (ПеО).

Проект настраивается через ПеО, достаточно указать их в файле `.env`.
Передача значений ПеО происходит с использованием [environs](https://pypi.org/project/environs/).

### Параметры проекта

|       Ключ        |     Назначение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`ALLOWED_HOSTS`| Разрешённые хосты |`['0.0.0.0', '127.0.0.1', 'localhost']`|
|`DEBUG`| Режим отладки |`False`|
|`INTERNAL_IPS`| Настройка для работы с [DDT](https://django-debug-toolbar.readthedocs.io/en/latest/index.html) |`[]`|
|`SECRET_KEY`| Уникальное непредсказуемое значение |-|

### Параметры подключения к БД

По умолчанию, используется СУБД SQLite.

|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`DATABASE_FILEPATH`| Абсолютный путь к БД | - |

## Установка

- клонировать проект,
- создать каталог виртуального окружения (ВО)*,
- связать каталоги ВО и проекта,
- установить зависимости:
```sh
git clone https://github.com/Padking/blog-sensive.git
cd blog-sensive
mkvirtualenv -p <path to python> <name of virtualenv>
setvirtualenvproject <path to virtualenv> <path to project>
pip install -r requirements.txt
```

- применение миграций к проекту:
```sh
python manage.py migrate
```

- создать суперпользователя в интерактивном режиме**,
- наполнить БД информацией о читателях блога через [Django admin site](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/),
- запустить сайт,
- перейти на [сайт](http://127.0.0.1:8000/admin/) для наполения БД,
- убедиться в отображении постов на главной странице [сайта](http://127.0.0.1:8000/).
```bash
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```



\* с использованием [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)

\** для наполнения БД через [Django admin site](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/)
