
# Django

## Теория

**Django это круто**.

Смотри почему здесь:
http://tutorial.djangogirls.org/ru/django/

Файловая структура django: apps и projects:
http://stackoverflow.com/questions/4879036/django-projects-vs-apps

## Практика

- Устанавливаем django
```python
pip install django
```
- Создаем проект
```python
django-admin startproject website
```

- Проверяем, что сайт запускается.
В папке `mai-student-life/website` вводим команду:
```python
python manage.py runserver
```
Переходим в браузере по адресу `localhost:8000`, видим, что всё работает

Теперь когда мы создали проект наша задача в том, чтобы создать:
- Создать *app*, который будет содержать функционал сообществ МАИ
- Модель студенческого сообщества МАИ
- Вид для отображения главной страницы
- Вид для отображения одного сообщества
- Шаблоны для отображения данных видов
- Настройки urls чтобы получить доступ к созданным видам

Создадим *app* сообществ.
В папке `mai-student-life/website` выполним команду:
```python
django-admin startapp communities
```

Добавим приложение в проект. Для этого просто добавим **`communities`** в список **`INSTALLED_APPS`** в `mai-student-life/website/website/settings.py`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'communities'
]
```

Создадим модель.
В папке `mai-student-life/website/communities` заполним файл `models.py`

```python
from django.db import models
COMMUNITY_TYPES = (
    ('reg','Regular'),
    ('hon', 'Honorary')
)

class Community(models.Model):
    created_date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=250, default="") 
    description = models.TextField(max_length=500, default="")
    vk_link = models.CharField(max_length=100, default="")
    contacts = models.TextField(max_length=300, default="")
    community_type = models.CharField(max_length=3, default='reg', choices=COMMUNITY_TYPES)
```

О полях для моделей см https://docs.djangoproject.com/en/1.9/ref/models/fields/

Чтобы управлять моделью через панель администрации откроем файл `mai-student-life/website/communities/admin.py` и заполним его:
```python
from django.contrib import admin

from .models import Community

admin.site.register(Community)
```

Теперь нам нужно добавить модель в базу данных. Для `sqlite3` это будет таблица `communities`.
Однако нам не нужно об этом задмуываться: Django сделает это за нас.

Создадим объект миграции - изменения базы данных. В папке `mai-student-life/website` выполним команду:
```python
python manage.py makemigrations
```
Получаем отчет о созданной миграции со списокм изменений.
Теперь выполним миграции - непосредственно применим изменения к схеме БД.
```python
python manage.py migrate
```

Итак у нас есть модель. 
Посмотрим на неё.
Создадим **superuser** для доступа к панели администрации.
В папке `mai-student-life/website`
```python
python manage.py createsuperuser
```

Снова запустим сервер и перейдем по адресу `localhost:8000/admin`, введем логин и пароль.
Мы можем создавать Сommunity и просматривать существующие.

Теперь сделаем так, что можно будет просматривать сообщества не только через панель администрации.

Создадим вид главной страницы в `mai-student-life/website/communities/views.py`
```python
from django.shortcuts import render, render_to_response
from .models import *
from django.template import RequestContext

def communities_list(request):
    template_name = 'community_list.html'
    community_list = Community.objects.all()
    return render_to_response(template_name, { "community_list": community_list }, context_instance=RequestContext(request))

def index(request):
    return communities_list(request)
```
Вид главной страницы (index) будет возвращать список сообществ.

Теперь создадим шаблон `mai-student-life/website/communities/community_list.html`
```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <title>MAI COMMUNITIES</title>
</head>
<body>	
    <div class='wrapper'>
        <header>
            <div  class="container">
                List of MAI communities
            </div>
        </header>
        <div class="content">
            {% for community in community_list %}
            <div class="community">
                <br/>
                    <h3>{{ community.title }}</h3>
                    <p>{{ community.description }}</p>
                    <p><a href="{{community.vk_link}}">{{ community.vk_link }}</a></p>
                    <p>{{ community.contacts }}</p>
                <br/>
            </div>

        </div>
    </div>
    <footer class="push">
        MAI COMMUNITIES
    </footer>
</body>
</html>
```

Всё почти готово, осталось только указать, по какому адресу (ссылке) можно получить доступ к виду, который в свою очередь вернет этот шаблон.

Для этого перейдем в файл `mai-student-life/website/website/urls.py`
В **url_patterns** добавим шаблон **url**, который будет переадресовывать пользователя на вид "*index*".
```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index")
]
```

Всё готово. Создадим сообщество "Лямбда" в панели администрации (`localhost:8000/admin`) и перейдем по адресу `localhost:8000`

Мы получили ~~уродливый~~ список сообществ!

В следующей лекции мы узнаем, как сделать его менее вырвиглазным.

## На дом:
Сделайте форк репозитория с сайтом.
Внесите следующие изменения:

1\. **Detail страница**  
Сделайте новый вид, шаблон и шаблон `url` для доступа к конкретному сообществу. Это должна быть страница, на которой отображается информация только одного сообщества. Ссылка может например быть такой: `localhost:8000/communities/X`, где **X** - `id` данного сообщества. Это называется `detail` страницой объекта. Добавьте в шаблон `communities_list` в заголовок каждого сообщества ссылку на его `detail` страницу.

Полезная ссылка: https://docs.djangoproject.com/en/1.9/intro/tutorial03/.


2\. **Правильный routing**
Измените маршрутизацию адресов (`routing`), то есть шаблоны `url_patterns`, так, чтобы в `website/communities` был свой файл `urls.py` содержащий текущий шаблон `url` для индекса ( `url(r"^$", views.index, name="index")` ), а файл `website/website/urls.py` просто на него ссылался.
Подсказка: это делается через `include`.

Всё что нужно здесь: http://tutorial.djangogirls.org/ru/django_urls/#твой-первый-urlадрес-в-django

Создайте **пулреквест**, чтобы обновить сайт в репозитории лямбды.

Удачи!
