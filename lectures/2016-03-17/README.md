
# ООП на Python 3

## Теория
**Объектно-ориентированное программирование (ООП)** — парадигма программирования, в которой основными концепциями являются понятия объектов и классов.

**Класс** — тип, описывающий устройство объектов. 

**Объект** — это экземпляр класса. Класс можно сравнить с чертежом, по которому создаются объекты. Объекты так же называют инстансами (англ *instance*).

Чтобы понятия класса и объекта были яснее можно привести несколько примеров.
Яблоко, апельсин и груша могут являться объектами одного класса - фрукт. 

В конце концов класс это коллекция (структура) данных, в случае создания новых классов - пользовательский тип данных. 
Так же класс это объединение данных и методов, тогда как при использовании структур (например `dict`) мы работаем только с данными.

## Практика
Представим, что мы делаем простейший форум и нам необходимо хранить данные о нескольких пользователях. Каждый пользователь уникален и имеет аналогичный другим набор информации: логин и пароль. Следовательно нам необходима структура данных для хранения этой информации.

Тогда мы создадим класс User, а все объекты этого класса будут уникальными пользователями.


```python
class User():
    user_type = "Regular"
    def __init__(self, login, password):
        self.login = login
        self.password = password
```

Разберем, что написали

```python
class User():
```
Ключевое слово `class` работает как `def`, но обозначает создание нового класса, а не метода.Сюда можно поместить переменные, общие для всех объектов класса.

------

```python
user_type = 'Regular'
```
Добавим поле `user_type` в целях демонстрации.

------

```python
def __init__(self, login, password):
```
**`def`** внутри объявления класса объявляет его метод. Методы с двумя поччеркиваниями (`__`) в начале и в конце являются служебными. Это не значит, что их не надо переопределять.  
**`init`** (полн. *initialize* - инициализировать, создать) определяет создание экземпляра класса - какие параметры должны подаваться на вход, через аргументы метода, для создания объекта класса. **`init`** принято называть конструктором класса.  
**`self`** - это ссылка на объект класса. **`self`** это обязательный первый аргумент любого метода, оперирующего объектом класса. **`self`** содержит пустой объект в **`init`**, в который можно записать данные.  
**`self.login`** - это поле `login` нового объекта класса `User`, а `login` справа - значение, переданное конструктору

------

Рассмотрим наглядно.
Класс объявлен и мы можем создать объект юзера.


```python
login = 'boris'
password = '12345'
first_user = User(login, password)

login = 'kolya'
password = '54321'
second_user = User(login, password)
```

Команда 
```python
first_user = User(login, password)
```
запускает метод `__init__` и возвращает полученный объект.

`first_user` и `second_user` содержат два разных объекта одного класса.


```python
print("User types: %s and %s" % (first_user.user_type, second_user.user_type)) 
```

    User types: Regular and Regular
    

Оба объекта вернут одно значение, хотя мы не вводили его в конструктор. Это поле общее для всех объектов класса.

Это так же значит, что если мы переопределим `user_type` у `first_user`, значение поменяется и у `second_user`. 


```python
print("User logins: %s and %s" % (first_user.login, second_user.login))
```

    User logins: boris and kolya
    

Логины разные, потому что это независимые друг от друга объекты.

------

Конечно же мы можем получить класс объекта


```python
print("Object classes: %s and %s" % (first_user.__class__, type(second_user)))
```

    Object classes: <class '__main__.User'> and <class '__main__.User'>
    

Ещё немного теории.

В **Python** всё является объектами - и строки, и списки, и словари, и всё остальное. Это значит, что у всего есть класс.

**ООП** как парадигма, независимо от языка, строится на четырех основных принципах. 
Скажем о них кратко:

1\. **Полиморфизм**: в разных объектах одна и та же операция может выполнять различные функции. Простым примером полиморфизма может служить оператор сложения. Выражение `1 + 1` производит сложение целых чисел, а `[1] + [1]` производит создание нового списка являющегося объединением "слагаемых" списков.  
В нашем случае полиморфизм можно продемонстрировать через вывод имени пользователя.  
Служебный метод `__str__` отвечает за преобразование объекта в строковый вид. Мы можем его переопределить


```python
class User():
    user_type = "Regular"
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __str__(self): #обратите внимание на self
        return self.login

login = 'boris'
password = '12345'
first_user = User(login, password)

login = 'kolya'
password = '54321'
second_user = User(login, password)
```

Логины этих юзеров можно получить как обратившись к полю `login`, так и сделав преобразование объекта в строку:


```python
print("User logins with __str__: %s and %s"%(str(first_user), second_user.login))
```

    User logins with __str__: boris and kolya
    

2\. **Инкапсуляция**: можно скрыть ненужные внутренние подробности работы объекта от окружающего мира.  
В нашем примере инкапсуляция может применяться при установке значения пароля и при запросе его значения. Например мы хотим зашифровать пароль при его записи и расшифровать при получении. Это скроет поле password от прямого доступа, оно будет доступно только через определенные методы.


```python
def encrypt(password):
    return password

def decrypt(password):
    return password
```

Методы шифрования и дешифровки я описывать не буду, используйте воображение и представьте, что они правда шифруют и дешифруют.


```python
class User():
    user_type = "Regular"
    def __init__(self, login, password):
        self.login = login
        self.set_password(password)

    def set_password(self, password):
        self.password = encrypt(password)

    def get_password(self, password):
        return decrypt(self.password)

    def __str__(self): #обратите внимание на self
        return self.login
```

3\. **Наследование**: можно создавать специализированные классы на основе базовых. Это позволяет нам избегать написания повторного кода.  
Представим, что нам нужно создать одного обычного пользователя и одного пользователя модератора.
Модератор имеет все те же данные, что и обычный пользователь (логин, пароль) плюс данные, которых не имеет обычный пользователь (раздел модерации). 
Чтобы не добавлять в класс User поля, которые нужны только модераторам, логично создать новый класс: Moderator.
Python позволяет классу Moderator наследоваться от User, а значит перенять все его свойства и при необходимости переопределить их.


```python
def encrypt(password):
    return password

def decrypt(password):
    return password

class User():
    user_type = "Regular"
    def __init__(self, login, password):
        self.login = login
        self.set_password(password)

    def set_password(self, password):
        self.password = encrypt(password)

    def get_password(self, password):
        return decrypt(self.password)
    
    def __str__(self):
        return self.login
```

Создадим новый класс, который будет наследовать свойства класса `User`


```python
class Moderator(User): 
    user_type = "Moderator"

    def __init__(self, login, password, forum_part):
        User.__init__(self, login, password)  # Сначала инициализируем базовый класс
        self.forum_part = forum_part

    def __str__(self):  # обратите внимание на self
        return  self.login + ' moderator of ' + self.forum_part
```

В скобках пишем имя класса, от которого наследуется данный класс
на самом деле когда мы не пишем ничего в скобках применяется наследование от базового класса, который и содержит __str__, __init__ и прочее.
Модератор так же наследует все методы Юзера такие как set_password, get_password. 


```python
login = 'boris'
password = '12345'
first_user = User(login, password)

login = 'kolya'
password = '54321'
forum_part = 'flood'
second_user = Moderator(login, password, forum_part)
```


```python
print("User and moderator with __str__: %s and %s"%(str(first_user), str(second_user)))
```

    User and moderator with __str__: boris and kolya moderator of flood
    

Коля получил повышение до модератора


```python
print("User and moderator logins: %s and %s"%(first_user.login, second_user.login))
```

    User and moderator logins: boris and kolya
    

Однако у Коли так же есть поле логин, хотя мы его и не обозначали в его конструкторе явно


```python
print("User and moderator user types: %s and %s"%(first_user.user_type, second_user.user_type)) 
```

    User and moderator user types: Regular and Moderator
    

Типы пользователей разные

------

Если нам надо узнать какого типа наш пользователь стоит воспользоваться `isinstance`


```python
if isinstance(first_user, Moderator):
    print("First user is a moderator!")
elif isinstance(second_user, Moderator):
    print("Second user is a moderator!")
else:
    print("No moderators!")
```

    Second user is a moderator!
    

4\. **Композиция**: объект может быть составным и включать в себя другие объекты.

------

## Особенности ООП в Python:
1. множественное наследование;
2. производный класс может переопределить любые методы базовых классов;
3. в любом месте можно вызвать метод с тем же именем базового класса;
4. все атрибуты класса в питоне по умолчанию являются public, т.е. доступны отовсюду; все методы — виртуальные, т.е. перегружают базовые.

Источники: 
+ [Объектно-ориентированное программирование. Общее представление](http://pythonworld.ru/osnovy/obektno-orientirovannoe-programmirovanie-obshhee-predstavlenie.html)
+ [Improve Your Python: Python Classes and Object Oriented Programming](https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/)
+ [Object Oriented Programming](http://anandology.com/python-practice-book/object_oriented_programming.html)
+ [Object Oriented Programming](http://www.python-course.eu/object_oriented_programming.php)
+ [Служебные методы, операторы и другое](http://pythonworld.ru/osnovy/peregruzka-operatorov.html)

## Домашнее задание       
Измените парсер из лекций 1 и 2 так, чтобы для каждого сайта в коде парсера существовал класс имеющий:
- метод `parse`, получающий на вход ничего и возвращающий список тайтлов книг
- метод `find_titles()`, получающий на вход `BeautifulSoup` объект и возращающий список тайтлов

Должен быть базовый класс Site, а каждый класс сайта должен от него наследоваться.
Вся индивидуальная логика парсинга конкретного сайта должна быть в классе этого сайта, логика относящаяся ко всем сайтам - в классе Site.
