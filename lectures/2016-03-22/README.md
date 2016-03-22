
# Исключения в Python
## Теория


```python
result = 1 / 0
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-1-3b10e2a1c32c> in <module>()
    ----> 1 result = 1 / 0
    

    ZeroDivisionError: division by zero


Если запустить этот код мы получим ошибку `ZeroDivisionError`.
Более корректно называть это исключением.

Существует (как минимум) два различимых вида ошибок: синтаксические ошибки (`syntax errors`) и исключения (`exceptions`).

Синтаксические ошибки, появляются во время разбора кода интерпретатором. С точки зрения синтаксиса в коде выше ошибки нет, интерпретатор видит деление одного `integer` на другой.

Однако в процессе выполнения возникает исключение. Интерпретатор разобрал код, но провести операцию не смог.
Таким образом ошибки, обнаруженные при исполнении, называются исключениями (`exceptions`). 

Исключения бывают разных типов и тип исключения выводится в сообщении об ошибке, например `ZeroDivisionError`, `NameError`, `ValueError`.

------

Давайте обрабатывать!

Существует возможность написать код, который будет перехватывать избранные исключения. Посмотрите на представленный пример, в котором пользователю предлагают вводить число до тех пор, пока оно не окажется корректным целым. Тем не менее, пользователь может прервать программу (используя сочетание клавиш `Control-C` или какое-либо другое, поддерживаемое операционной системой).

Заметьте — о вызванном пользователем прерывании сигнализирует исключение `KeyboardInterrupt`.


```python
while True:
    try:
        x = int(input("Input a number:"))
        break
    except ValueError:
        print("Incorrect integer")
```

    Input a number:fourty two
    Incorrect integer
    Input a number:42
    

Оператор `try` работает следующим образом:  
В начале исполняется блок `try` (операторы между ключевыми словами `try` и `except`).
Если при этом не появляется исключений, блок `except` не выполняется и оператор `try` заканчивает работу.
Если во время выполнения блока `try` было возбуждено какое-либо исключение, оставшаяся часть блока не выполняется. Затем, если тип этого исключения совпадает с исключением, указанным после ключевого слова `except`, выполняется блок `except`, а по его завершению выполнение продолжается сразу после оператора `try-except`.
Если порождается исключение, не совпадающее по типу с указанным в блоке `except` — оно передаётся внешним операторам `try`; если ни одного обработчика не найдено, исключение считается необработанным (`unhandled exception`), и выполнение полностью останавливается и выводится сообщение об ошибке.

Блок `except` может указывать несколько исключений в виде заключённого в скобки кортежа.


```python
try:
    x = int(input("Input another number:"))
except (RuntimeError, TypeError, NameError, ValueError):
    print("Caught an exception")
```

    Input another number:not a number
    Caught an exception
    

В последнем блоке `except` можно не указывать имени (или имён) исключений. Тогда он будет действовать как обработчик всех исключений. 


```python
while True:
    try:
        x = int(input("Input a number:"))
        break
    except:
        print("Incorrect integer")
```

    Input a number:not a number
    Incorrect integer
    Input a number:42?
    Incorrect integer
    Input a number:42
    

Получить доступ к информации об исключении можно используя `sys.exc_info()[0]`


```python
import sys
while True:
    try:
        x = int(input("Input a number:"))
        break
    except:
        print("Caught exception:",sys.exc_info()[0])
```

    Input a number:wow, such an exception
    Caught exception: <class 'ValueError'>
    Input a number:34
    

Более простой способ: записать экземпляр исключения в переменную


```python
while True:
    try:
        x = int(input("Input a number:"))
        break
    except ValueError as e: 
        print("Incorrect integer", e)
```

    Input a number:much integer
    Incorrect integer invalid literal for int() with base 10: 'much integer'
    Input a number:88
    

Исключения могут охватывать несколько уровней.

При возбуждении исключения оно передается "вверх" пока не достигнет самого высокого уровня или не будет "поймано" блоком `except`.

Это значит, что исключения внутри функции не вызовут ошибку, если функция будет в блоке `try-except`:


```python
def zero_division():
    return 1/0

try:
    zero_division()
except:
    print("Caught exception")
```

    Caught exception
    

Можно увеличить вложенность 


```python
def level_3():
    return 1/0

def level_2():
    return level_3()

def level_1():
    return level_2

try:
    level_1()
except:
    print("Caught exception")
```

Можно порождать свои исключения оператором `raise`


```python
try:
    raise(Exception("amazing!"))
except Exception as e:
    print(e)
```

    amazing!
    

Можно добавить в блок `try-except` блоки `else` и `finally`.

Блок `else` будет выполнен если `try` не породил исключений.

Блок `finally` будет выполнен в любом случае.


```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Zero division!")
    else:
        print("Result ", result)
    finally:
        print("finally")

print(divide(1,2))
print(divide(1,0))
```

Можно создавать собственные исключения - для этого нужно объявить новый класс, наследующийся от `Exception`.


```python
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)
```

    My exception occurred, value: 4
    

# Модули в Python

Импоритируем лежащий в том же каталоге файл `test_module.py`


```python
import test_module
print('Type of object: %s'%(str(type(test_module))) )
```

    test module has been imported
    Type of object: <class 'module'>
    

Теперь `test_module` это объект типа `module`, то есть модуль Python.

Атрибуты модуля - переменные, функции и классы, объявленые в файле, доступны нам как атрибуты класса


```python
print('\nAccesing module attributes:')
test_module.func1()
test_module.func2()

print('X equals: %s'%(str(test_module.x)))
print('Y equals: %s'%(str(test_module.y)))
print('Class atr: %s'%(str(test_module.MyClass.test_atr)))
```

    
    Accesing module attributes:
    Func 1
    Func 2
    X equals: 1
    Y equals: 2
    Class atr: Lambda
    

Второй вариант импорта — взятие непосредственно имени без имени модуля.

Импорт на основе from обладает такой особенностью, что он делает импортируемые атрибуты `read-only`.


```python
from test_module import func1, func2, x
print('\nAccesing attributes with a different import:')
func1()
func2()

x = 10
print("X equals:",x)
print("Module x equals", test_module.x)
```

    
    Accesing attributes with a different import:
    Func 1
    Func 2
    X equals: 10
    Module x equals 1
    

В данном случае `x` — это локальная переменная, в то время как переменные `x` в модуле не меняются.

Можно задать alias ипортируемому имени для упрощения или избежания конфликта имен


```python
import test_module as md
print('\nImporting with alias')
print("Module x equals", md.x)

from test_module import func1 as f1
f1()
```

    
    Importing with alias
    Module x equals 1
    Func 1
    

Для выяснения имен, определенных в модуле, можно использовать встроенную функцию `dir()`. Она возвращает отсортированный список строк.

У модулей есть различные атрибуты, например `__doc__` выведет документацию к модулю. В нашем случае это будет многострочный комментарий в начале файла.


```python
print('\nUsing dir:')
print(dir(test_module))
with open('out.txt', "w", encoding='utf-8') as f:
    f.write(test_module.__doc__)
```

    
    Using dir:
    ['MyClass', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'func1', 'func2', 'x', 'y']
    

**Пакеты** (`packages`)

Пакеты — способ структурирования пространств имен модулей на основе файловой системы. Пакетная организация дает все удобства по управлению большим количеством файлов. Пакетный импорт делает код более читабельным и значительно упрощает поиск. 
Пример:

```    
       TCP/
             _init_.py
             main.py
       Server/
             _init_.py
             tcp.py
             server.py
             lib.py
       Client/
             _init_.py
             tcp.py
             client.py
             lib.py
```

Файл `_init_.py` необходим для того, чтобы интерпретатор распознал каталог, как содержащий пакет.
Этот файл может быть пустым. В этом файле обычно содержится информация о пакете (автор, версия, контакты и другое).

Мы можем импортировать тестовый модуль из пакета например так


```python
from test_package import package_test_module as ptm
print('\nImporting from package')
print("Module x equals", ptm.x)
```

    test module has been imported
    
    Importing from package
    Module x equals 100
    

Или так


```python
import test_package.package_test_module as ptm
print('\nImporting from package 2')
print("Module x equals", ptm.x)
```

    
    Importing from package 2
    Module x equals 100
    

Или так


```python
from test_package import *
print('\nImporting from package 3')
print("Module z equals", package_test_module.z)
```

    
    Importing from package 3
    Module z equals 300
    

Что означает импорт всех имен из пакета.

Этот вариант работает только если в `__init__` файле пакета определен список `__all__` , в котором перечисляются модули, которые импортируются в этом случае. 

```python
__all__ = ["package_test_module"]
```

## Источники: 
- [Ошибки и исключения](http://pep8.ru/doc/tutorial-3.1/8.html)
- [Программирование на Python: Часть 5. Модули](https://www.ibm.com/developerworks/ru/library/l-python_part_5/)
- [The import system](https://docs.python.org/3/reference/import.html)
- [Modules](https://docs.python.org/3/tutorial/modules.html)

## Домашнее задание:
- добавить обработку исключений в парсер, чтобы программа не "вылетала" при неудачных попытках читать и писать несуществующие или заблокированные файлы (исключение `IOError` например).
- Измените любой свой (или не свой, по желанию) проект, разделив его функционал на несколько файлов. Например в одном файле интерфейс, в другом функционал, в третьем вспомогательные функции.
