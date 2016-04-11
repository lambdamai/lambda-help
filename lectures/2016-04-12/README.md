
__Attention!__ Чтобы следить за ходом лекции нужно работать с данной версией репозитория:
https://github.com/lambda-frela/mai-student-life/tree/175f928d6e9ff72501cc6b1d2b1d38c9f986d426

# Шаблоны

Познакомимся поподробнее с шаблонами.
Первое дело: тэг `{% include %}`

В наших шаблонах присутствует повторяющийся HTML. Это например контейнер `<head>`, подключение обертка (_wrapper_) вокруг контента, _footer_.
Философия Django утверждает, что ничто не должно повторяться и быть неудобным. 
Поэтому существует простой инструмент для того, чтобы исправить ситуацию.

Создадим в __`communities/templates`__ шаблон __`base.html`__ и поместим туда скелет любой нашей страницы.

```html
<!DOCTYPE html>
<html lang="ru">
<head>

	<script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
	
    <title></title>
    <meta name="description" content="">
</head>
<body>	
	<header>
		<div  class="container">
		</div>
	</header>
	<div>
		<div  class="container">
			<div id="messages">
		
			</div>
		    <div class="content">

			</div>
		</div>
	</div>
	<footer class="push">
		<div class="container">
		</div>
	</footer>
</body>
</html>
```

Сразу подключаем __jquery__. Именно в контейнере _head_ мы будем подключать все внешние скрипты, таблицы стилей. Там же мы указываем необходимое для опознания нашего сайта поисковыми системами: _title_ и _description_ - имя и описание страницы.

Этот код будет скелетом. Мы должны указать куда в нём будет "подставляться" контент определенной страницы.

```html
<!DOCTYPE html>
<html lang="ru">
<head>

	<script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
	
    <title>{% block title %}{% endblock %}</title>
    <meta name="description" content="{% block description %}{% endblock %}">
</head>
<body>	
	<header>
		<div class="container navbar">
		</div>
	</header>
	<div>
		<div  class="container">
			<div id="messages">
		
			</div>
		    <div class="content">
		    	{% block content %}{% endblock %}
			</div>
		</div>
	</div>
	<footer class="push">
		<div class="container">
		</div>
	</footer>
</body>
</html>
```

Далее откроем наш существующий шаблон __community_list.html__ и изменим его на следующее.
```html
{% extends "base.html" %}
{% block title %}MAI COMMUNITIES{% endblock %}
{% block description %}
Curated list of MAI student communities.
{% endblock %}
{% block content %}
    <div class="communities-list">
        {% for community in community_list %}
            <div class="community">
                <br/>
                <h3><a href="{% url 'communities:community_detail' community.pk %}">{{ community.title }}</a></h3>
                <p>{{ community.description }}</p>
                <p><a href="{{ community.vk_link }}">{{ community.vk_link }}</a></p>
                <p>{{ community.contacts }}</p>
                <br/>
            </div>
        {% endfor %}
    </div>
    {% if community_list.paginator.num_pages > 1 %}
        <div class="pagination">
            {% if community_list.has_previous %}
                <a href="?page={{ community_list.previous_page_number }}">←</a>
            {% endif %}

            {% for num in community_list.paginator.page_range %}
                {% if num == community_list.number %}
                    <span class="current"><b>{{ num }}</b></span>
                {% else %}
                    <a href="?page={{ num }}"> {{ num }}</a>
                {% endif %}
            {% endfor %}

            {% if community_list.has_next %}
                <a href="?page={{ community_list.next_page_number }}">→</a>
            {% endif %}
        </div>
    {% endif %}
{% endblock  %}
```

Итак, что произойдет, если _Django_ в ответ на запрос пользователя "отрисует" шаблон __community_list.html__?
1. Из-за тэга _extends_ за основу будет взят указанный шаблон ("__base.html__"). 
2. Блоки основного шаблона (_title_, _description_, _content_) буду заполнены содержимым из шаблона __community_list__.
Например в тэг `<title>` в контейнере `<head>` будет записана строка _"MAI COMMUNITIES"_.

Это дает нам определенные плюсы: мы не переписываем HTML код и в каждом шаблоне определяем только какой будет выводиться контент.

Однако это не всё. Сейчас код отрисовки одного сообщества в *community_list* и в *community_detail* совпадает. Совпадает значит повторяется. Это плохо.

Нам было бы удобно вынести его в отдельный шаблон, чтобы мы могли подавать ему на вход объект _community_ и получать отрисовку одного сообщества. Плюс такого решения в том, что мы могли бы использовать один и тот же шаблон несколько раз в разных местах не переписывая его. К тому же так просто красивее. Так же стоит поступать с пагинацией - вынести её в отдельный шаблон.

В этом нам поможет тэг `{% include %}`.

Создадим новый шаблон __community_card.html__
```html
<div class="community-card">
    <h3><a href="{% url 'communities:community_detail' community.pk %}">{{ com.title }}</a></h3>
    <p>{{ com.description }}</p>
    <p><a href="{{ com.vk_link }}">{{ com.vk_link }}</a></p>
    <p>{{ com.contacts }}</p>
</div>
```
Да, это весь код, который должен в нём содержаться.

Теперь изменим __community_list.html__

```html
{% extends "base.html" %}
{% block title %}MAI COMMUNITIES{% endblock %}
{% block description %}
Curated list of MAI student communities.
{% endblock %}
{% block content %}
    <div class="communities-list">
        {% for community in community_list %}
            {% include "community_detail.html" with com=community %}    
        {% endfor %}
    </div>
    {% if community_list.paginator.num_pages > 1 %}
        <div class="pagination">
            {% if community_list.has_previous %}
                <a href="?page={{ community_list.previous_page_number }}">←</a>
            {% endif %}

            {% for num in community_list.paginator.page_range %}
                {% if num == community_list.number %}
                    <span class="current"><b>{{ num }}</b></span>
                {% else %}
                    <a href="?page={{ num }}"> {{ num }}</a>
                {% endif %}
            {% endfor %}

            {% if community_list.has_next %}
                <a href="?page={{ community_list.next_page_number }}">→</a>
            {% endif %}
        </div>
    {% endif %}
{% endblock  %}
```

Мы вынесли кусок кода в отдельный шаблон и вставляем его через `{% include %}`, передавая ему переменную _community_.
Заметьте конструкцию `{% include "community_detail.html" with com=community %}`.
В данном случае `with com=community` означает "передать в шаблон пемеренную community и записать её значение в локальную переменную _com_". Однако если мы заменим com на community в шаблоне __community_card.html__ нам не потребуется указывать `with`: Джанго атвоматически передаст значение переменной _community_ потому что она имеет одинаковое имя в обоих шаблонах. 

Аналогино создадим шаблон pagination.html 
```html
{% if paginated_list.paginator.num_pages > 1 %}
    <div class="pagination">
        {% if paginated_list.has_previous %}
            <a href="?page={{ paginated_list.previous_page_number }}">←</a>
        {% endif %}

        {% for num in paginated_list.paginator.page_range %}
            {% if num == paginated_list.number %}
                <span class="current"><b>{{ num }}</b></span>
            {% else %}
                <a href="?page={{ num }}"> {{ num }}</a>
            {% endif %}
        {% endfor %}

        {% if paginated_list.has_next %}
            <a href="?page={{ paginated_list.next_page_number }}">→</a>
        {% endif %}
    </div>
{% endif %}
```

И вставим его на место пагинации.
```html
{% extends "base.html" %}
{% block title %}MAI COMMUNITIES{% endblock %}
{% block description %}
Curated list of MAI student communities.
{% endblock %}
{% block content %}
    <div class="communities-list">
        {% for community in community_list %}
            {% include "community_detail.html" with com=community %}  
        {% endfor %}
    </div>
    {% include "pagination.html" with paginated_list=community_list %}  
{% endblock  %}
```

Так же изменим шаблон __community_detail.html__:
```html
{% extends "base.html" %}
{% block title %}MAI COMMUNITY {{community.name}}{% endblock %}
{% block description %}
{{community.description}}
{% endblock %}
{% block content %}
    {% include "community_card.html" %}
{% endblock  %}
```

Заметье, что теперь мы используем динамические значения блоков _title_ и _description_: туда подставляется название сообщества и его описание. 

Итак мы сократили код примерно вдвое.

## Небольшое задание для запрепления:
	
1. Создайте страницу "__about.html__" со статичной текстовой информацией о сайте. Заполните её чем угодно. Для создания страницы необходимо создать новый вид, шаблон и добавить ссылку на вид в __website/urls.py__. Бонусные очки если вы создадите файл __views.py__ и папку _templates_ в проекте _website_. Функционал страницы _about_ не относится к студенческим сообществам - он относится к проекту, поэтому будет разумно расположить его в _website_, а не в приложении _communities_.

2. Создайте шаблон "__navbar.html__" который будет содержать список (`<ul>`) из двух ссылок: на страницу _about_ и на страницу _home_ (_index_). Вставьте этот шаблон в __base.html__ через `{% include %}`, чтобы навигационная панель выводилась на любой странице сайта.

# Добавим свой CSS, интегрируем Bootstrap.

Чтобы сделать сайт красивым или хотя бы читабельным нам нужны таблицы стилей, то есть CSS.

Чтобы добавлять CSS, JS и другие статичные файлы добавим директорию для статичных файлов в __settings.py__ нашего проекта, а так же ссылка по которой эти файлы будут доступны.
```python
STATIC_URL = '/static/'
PROJECT_DIR = os.path.dirname(__file__)
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'staticfiles'),
)

```

Теперь создадим в папке __website/website__ директорию __staticfiles__, а в ней файл __theme.css__.

Добавим в этот файл стиль для демонстрации:
```css
h3 {
  font-style:bold;
  font-size:20pt;
}
```
Осталось только подключить файл.

Добавим в шаблон "__base.html__", в контейнер _head_ следующую конструкцию:

```html
{% load static %}
<link href="{% static 'css/theme.css' %}" rel="stylesheet"></link>
```

Заголовки сообществ стали заметно больше, а мы подключили свой первый стиль.

Однако нам не нужно создавать дизайн сайта прописывая все стили самим. Существует комплект полезных компонентов - __Bootstrap__ - который сделает это за нас.

Установим его как пакет Python. 
В командной строке введем:
```
pip install django-bootstrap3
```

Теперь просто добавим его название в website/website/settings.py INSTALLED_APPS

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'communities',
    'bootstrap3'
]
```

И добавим его в контейнер `<head>` в base.html

```html
{% load bootstrap3 %}
{% bootstrap_css %}
{% bootstrap_javascript %}

```

Мы ещё ничего не сделали, а сайт уже выглядит лучше.
Теперь мы можем использовать компоненты Bootstrap чтобы навести красоту

http://getbootstrap.com/css/

Красивые кнопки, кроссбраузерность, автоматическая адаптация под мобильные телефоны и многое другое.

Задание на дом:

1. Сделать коммит изменений с созданием страницы _about_ и шаблона _navbar_. Оформить _pull request_ в основной репозиторий Лямбда, чтобы изменения были синхронизированы.

2. Оформить _navbar_ с помощью компонентов Bootstrap - http://getbootstrap.com/components/#navbar
		

3. Оформить __community_card.html__ с помощью панелей Bootstrap - http://getbootstrap.com/components/#panels
		

4. Оформить __pagination.html__ с помощью пагинации Bootstrap - http://getbootstrap.com/components/#pagination

5. Сделать так, чтобы на странице _about_ кнопка перехода на эту страницу в _navbar_ светилась ярко синим цветом, а на странице _home_ светилась кнопка _home_. Иначе говоря необходимо:
    - Создать стиль `.active` в __theme.css__
    - Применять этот стиль к кнопке активной страницы в __navbar.html__

6. __Дополнительное задание__
Сделать возможным [загрузку одного изображения](http://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example) для каждого сообщества. Сделать вывод этого изображения в панелях сообществ.

Как всегда, все изменения нужно закомитить в свой репозиторий, а затем оформить pull request в основной репозиторий Лямбда!

Если вам что-то непонятно вы всегда можете спросить в рабочем чате в телеграмм.
