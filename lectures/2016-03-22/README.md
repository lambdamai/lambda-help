
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

    Input a number:Hello, world!
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

    Input another number:memes
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

    Input a number:Not a number
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

    Input a number:definitely not a number
    Incorrect integer invalid literal for int() with base 10: 'definitely not a number'
    Input a number:44
    

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

    Result  0.5
    finally
    None
    Zero division!
    finally
    None
    

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

## Источники: 
- [Ошибки и исключения](http://pep8.ru/doc/tutorial-3.1/8.html)

## Домашнее задание:
добавить обработку исключений в парсер, чтобы программа не "вылетала" при неудачных попытках читать и писать несуществующие или заблокированные файлы (исключение `IOError` например).
