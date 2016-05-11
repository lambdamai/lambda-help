
## Что?

Djano REST framework позволяет удобно и просто добавить REST API к нашему проекту.
Это позволит разработчикам использовать наш контент в своих приложениях. 
Грубо говоря это ещё один интерфейс доступа к нашей базе данных.

Как это работает можно посмотреть здесь:
http://restframework.herokuapp.com/

Наглядно и красиво.

## Поехали

Перед тем, как мы начнем, убедимся, что у нас есть [проект mai-student-life от 11.05.2016](https://github.com/lambda-frela/mai-student-life/tree/8c4b709daa041d272d8ce0f7e5209b989532eb67). Если нет - скачиваем или клонируем.

Мы добавим простой REST API который позволит получать информацию о сообществах.

Для начала установим **django rest framework**. 
В консоли системы введем:

```
pip3 install djangorestframework
```
Мы установили пакет, теперь добавим его в проект.
В `project/website/settings` добавим его в `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'common',
    'community',
    'bootstrap3',
    'rest_framework'
]
```

Мы готовы начинать.

У нас есть модель Community и мы хотим предоставить всем юзерам доступ к ней через REST API.

### Сериализатор

Нам нужно создать сериализатор - класс, который отвечает за преобразование данных в json формат. Чтобы мы не нароком не начали думать своей головой и писать свой код django rest framework делает почти всё за нас. Сериализаторы создаются почти как Django формы.
Создадим файл `project/community/serializers.py`.
И заполним его:
```python
from .models import Community
from rest_framework import serializers

class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Community
        fields = ('created_date', 'title','description','vk_link','contacts','community_type')
```

Класс serializers.HyperlinkedModelSerializer добавит при выводе экземпляря сообщества прямую ссылку на него. 
Согласно [документации](http://www.django-rest-framework.org/api-guide/serializers/#how-hyperlinked-views-are-determined) для определения нужной ссылки класс будет искать вид с именем `community-detail` принимающий на вход ключ `pk`.
Мы можем явно указать какой вид искать.

```python
from .models import Community
from rest_framework import serializers

class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='community:detail',
        lookup_field='pk'
    )
    class Meta:
        model = Community
        fields = ('pk', 'url', 'created_date', 'title','description','vk_link','contacts','community_type')
```

Заметьте, что поля `url` нет в нашей модели, но API его выведет. Мы должны сделать так, чтобы сериализатор мог получить значение этого поля. Для этого мы указываем какой вид ему требуется найти через название вида и принимаемые аргументы (`community:detail', 'pk').

Требуется внести некоторые корректировки в существующие ссылки и виды:

1\. Добавим `namespace` для `community`. В `project/website/urls.py':  
Заменить

```python
    url(r'^community/', include('community.urls')),
```

на

```python
    url(r'^community/', include('community.urls', namespace='community')),
```

[Зачем?](https://docs.djangoproject.com/en/1.9/topics/http/urls/#introduction)

2\. Отредактируем ссылки и вид, чтобы сериализатор мог определить из какого вида получать `url`.  В `project/community/urls.py`:  
Заменим
```python
    url(r'^detail/(?P<community_id>[0-9]+)/$', views.detail, name='detail'),
```

на

```python
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
```

В `project/community/views.py`:  
Заменим
```python
def detail(request, community_id):
    template_name = 'community/detail.html'
    community = Community.objects.get(pk=community_id)
    return render(request, template_name, {"community": community})
```
на
```python
def detail(request, pk):
    template_name = 'community/detail.html'
    community = Community.objects.get(pk=pk)
    return render(request, template_name, {"community": community})
```

Суть не изменилась, но теперь сериализатор сможет выводить поле url.

### Вид

Создадим вид, который будет обращаться к созданному сериализатору.
Изменим файл `project/community/views.py`:

```python
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import CommunitySerializer

def community_list(request):
    template_name = 'community/list.html'
    paginator = Paginator(Community.objects.all(), 5)

    try:
        items = paginator.page(request.GET.get('page'))
    except (PageNotAnInteger, EmptyPage):
        items = paginator.page(1)

    return render(request, template_name, {"community_list": items})


def detail(request, community_id):
    template_name = 'community/detail.html'
    community = Community.objects.get(pk=community_id)
    return render(request, template_name, {"community": community})

class CommunityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows communities to be viewed.
    """
    queryset = Community.objects.all().order_by('-created_date')
    serializer_class = CommunitySerializer
```

Здесь используется новый концепт - `ViewSet`. `ViewSet` просто объединяет типичный функционал в один класс, при этом мы всегда можем разбить его на индивидуальные виды. В данном случае `ViewSet` объединяет функционал связанный с моделями: получение, добавление, изменение, удаление (вспоминаем составляющие REST: GET, PUT, UPDATE, DELETE ) и другое.
Из [документации](http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset):
> The actions provided by the ModelViewSet class are `.list()`, `.retrieve()`, `.create()`, `.update()`, and `.destroy()`.

### Ссылки

Необходимо обеспечить доступ к написанному виду.
Переходим в `project/community/urls.py`:
```python
from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'community', views.CommunityViewSet)

app_name = 'community'

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^list/$', views.community_list, name='list'),
    url(r'^detail/(?P<community_id>[0-9]+)/$', views.detail, name='detail'),
]
```

Здесь мы используем `Router`. Этот класс автоматически сгенерирует ссылки на основе данных из `CommunityViewSet`. 
Подробнее [в доках](http://www.django-rest-framework.org/api-guide/routers/).

### Последний штрих

Настроим наш API в `project/website/settings.py`. Добавим туда следующий код:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
       'rest_framework.permissions.AllowAny',
    ),
    'PAGE_SIZE': 10
}
```

Осталось только протестировать!
Для этого нам нужно сделать GET запрос с заголовком (header) `Accept: application/json`.
Откроем в любой папке консоль, запустим там python и выполним следующий код:
```python
import requests
url = `http://localhost:8000/community/community/`
headers = {'content-type': 'application/json'}
r = requests.get(url, headers=headers)
```
Мы используем библиотеку requests, которая позволяет делать HTTP запросы.
Теперь посмотрим, что вернул сервер:
```python
>>> r
<Response [200]>
>>> r.text
'{"count":0,"next":null,"previous":null,"results":[]}'
```
Долгожданный JSON!
Если мы добавим через панель администрации сообщества то сможем рассмотреть их подробнее.
```python
>>> r = requests.get(url, headers=headers)
>>> r.text
'{"count":1,"next":null,"previous":null,"results":[{"pk":1,"url":"http://localhost:8000/community/1.","create
d_date":"2016-05-11T11:55:36.873600Z","title":"Lambda","description":"MAI IT","vk_link":"http://vk.com/lambdaf
rela","contacts":"http://vk.com/lambdafrela","community_type":"hon"}]}'
```
Можно посмотреть на каждое сообщество отдельно
```python
>>> url = 'http://localhost:8000/community/community/1'
>>> r = requests.get(url, headers=headers)
>>> r.text
'{"pk":1,"url":"http://localhost:8000/community/1/","created_date":"2016-05-11T11:55:36.873600Z","title":"Lamb
da","description":"MAI IT","vk_link":"http://vk.com/lambdafrela","contacts":"http://vk.com/lambdafrela","commu
nity_type":"hon"}'
```
Если мы перейдем по ссылке `http://localhost:8000/community/community/1` в браузере, то увидим нормальный HTML, а здесь получаем JSON. (Почему так?)

## Заключение

Django REST Framework очень массивная и крутая штука, которая может облегчить жизнь при разработке любого приложения. Здесь была раскрыта лишь маленькая часть возможностей фреймворка. Если вам интересно изучать его дальше, то следует обратиться к [обучающим материалам](http://www.django-rest-framework.org/tutorial/1-serialization/).
