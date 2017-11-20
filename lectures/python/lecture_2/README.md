
![](pics/presentation.png)

# План на сегодня

- инкрементирование
- циклы
- работа с файлами
- синтаксический сахар

# Операторы ин- и декремента

![](http://devhumor.com/content/uploads/images/October2017/increment.jpg)

Инкремент, инкрементирование (от англ. _increment_ «увеличение») — операция во многих языках программирования, увеличивающая переменную. Обратную операцию называют декремент (уменьшение).

`i = i + 1`       <==>         `i += 1`     <==>         `i++`


```python
a = 5

a += 5
print(a)

a -= 5
print(a)

a *= 5
print(a)

a //= 5
print(a)
```

    10
    5
    25
    5
    

# Циклы

> Цикл — разновидность управляющей конструкции, предназначенная для организации многократного исполнения набора инструкций.

## For – Цикл со счётчиком

Цикл со счётчиком — цикл, в котором некоторая переменная изменяет своё значение от заданного начального значения до конечного значения с некоторым шагом, и для каждого значения этой переменной тело цикла выполняется один раз.

Общий вид:
```python
for counter in range(start, stop, step):
    expression
```


```python
# пример
for i in range(1,5):
    print(i)
```

    1
    2
    3
    4
    

Еще один вид циклов со счетчиками – [совместные циклы](https://ru.wikipedia.org/wiki/%D0%A6%D0%B8%D0%BA%D0%BB_(%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)). Такой цикл задает выполнение некоторой операции для объектов из заданного множества, без явного указания порядка перечисления этих объектов. Такие циклы называются совместными (а также циклами по коллекции, циклами просмотра) и представляют собой формальную запись инструкции вида: «Выполнить операцию `X` для всех элементов, входящих во множество `M`».

Общий вид:

```python
for item in iterable:
    expression
```
Где `iterable` – итерируемый объект (коллекция). В роли такого объекта могут выступать строки (`str`), списки (`list`), кортежи (`tuple`), а также любой [класс, объявленный с методом `__iter__()`](https://docs.python.org/3/glossary.html#iterable) (об этом в других лекциях).


```python
# пример на списке
MAI = ['я', 'мы', 'лучшие люди страны']

for people in MAI:
    print(f'МАИ - это {people}')
```

    МАИ - это я
    МАИ - это мы
    МАИ - это лучшие люди страны
    


```python
# жуткие вещи, дальше объясняются
list(map(lambda word: print(word), MAI))
```

    я
    мы
    лучшие люди страны
    




    [None, None, None]



Можно итерироваться по строке


```python
for letter in 'long_word':
    print(letter)
```

    l
    o
    n
    g
    _
    w
    o
    r
    d
    

Также можно итерироваться по числовой последовательности


```python
for i in range(1, 5):
    print(f'{i} muffins')
```

    1 muffins
    2 muffins
    3 muffins
    4 muffins
    

Если хочется внутри цикла обращаться к элементам коллекции по их индексам, можно использовать следующую конструкцию:

```python
X = range(1, 100, 2)

for i in range( len(X) ):
    print( X[i] )
```

Что тут произошло?
- X – список из некоторых данных
- `len(X)` - функция, возвращающая длину списка
- `range(len(X))` - создает коллекцию из индексов списка X
- `X[i]` - обращение к i-тому элементу коллекции

Такой метод итерации считается не очень красивым, логичным и не подходит под Python-way. Раз есть более элегантные способы итерации, то для поддержки читаемого кода рекомендуется использовать их.

Команда `enumerate(list)` принимает в качестве аргумента коллекцию (список) и возвращает список кортежей, каждый из которых содержит индекс элемента и его содержимое. 


```python
list(enumerate(MAI))
```




    [(0, 'я'), (1, 'мы'), (2, 'лучшие люди страны')]



Итерация по одной переменной `people` в таком случае будет возвращать те самые кортежи:


```python
for people in enumerate(MAI):
    print(people)
```

    (0, 'я')
    (1, 'мы')
    (2, 'лучшие люди страны')
    

Если же надо "распаковать" кортежи, то можно перечислить итерируемые переменные через запятую:


```python
for index, value in enumerate(MAI):
        print(f'index = {index}, value = {value}')
```

    index = 0, value = я
    index = 1, value = мы
    index = 2, value = лучшие люди страны
    

Однако на практике, скорее всего захочется итерироваться по содержимому одновременно нескольких коллекций, например по списку фамилий студентов и групп, в которых они учатся (**важно** – коллекции должны иметь одинаковую размерность). Если мы просто перечислим желаемые коллекции через запятую, то интерпретатор нас не одобрит:


```python
MAI = {1:'авиастроение', 'инжэкин':5, 9:'прикладная механика'}

for key, value in MAI.keys(), MAI.values():
    print('ключ "{0}"\t со значением "{1}"'.format(key, value))
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-8-f328d3f97fa9> in <module>()
          1 MAI = {1:'авиастроение', 'инжэкин':5, 9:'прикладная механика'}
          2 
    ----> 3 for key, value in MAI.keys(), MAI.values():
          4     print('ключ "{0}"\t со значением "{1}"'.format(key, value))
    

    ValueError: too many values to unpack (expected 2)


Это связано с тем, что объект, по которому происходит итерация **должен быть один**.

Что же делать?

Здесь на помощь приходит команда `zip()`, которая "упаковывает" две коллекции в одну для совместной итерации.


```python
print(f"""
    Ключи = { MAI.keys() },\n
    Значения = { MAI.values() },\n
    Вместе = { list(zip(MAI.keys(), MAI.values())) }
    """
)
```

    
        Ключи = dict_keys([1, 'инжэкин', 9]),
    
        Значения = dict_values(['авиастроение', 5, 'прикладная механика']),
    
        Вместе = [(1, 'авиастроение'), ('инжэкин', 5), (9, 'прикладная механика')]
        
    


```python
for key, value in zip(MAI.keys(), MAI.values()):
    print('ключ "{0}"\t со значением "{1}"'.format(key, value))
```

    ключ "1"	 со значением "авиастроение"
    ключ "инжэкин"	 со значением "5"
    ключ "9"	 со значением "прикладная механика"
    

## While – Цикл с предусловием

Цикл с предусловием — цикл, который выполняется, пока истинно некоторое условие, указанное перед его началом. Это условие проверяется **до** выполнения тела цикла, поэтому тело может быть не выполнено ни разу (если условие с самого начала ложно).

```python
while condition:
    loop_body
```

Общий вид (аналог функции $\displaystyle s=\sum_{i=1}^{100} i^2$)


```python
s = 0
i = 1

while i <= 100:
    s += i**2
    i += 1

print(s)
```

    338350
    

Вечный цикл

```python
while 1:
    pass
```

### _task_

Чему будет равна переменная i ?

```python
i = 0
while i <= 10:
    i += 1
    if i > 7:
        i += 2
```

Ответ: __13__

## Операторы `break` и `continue`

### `break` – Досрочный выход из цикла
Команда досрочного выхода применяется, когда необходимо прервать выполнение цикла, в котором условие выхода ещё не достигнуто. Такое бывает, например, когда при выполнении тела цикла обнаруживается ошибка, после которой дальнейшая работа цикла не имеет смысла. Её действие аналогично действию команды безусловного перехода (`goto`) на команду, непосредственно следующую за циклом, внутри которого эта команда находится. Но так как использовать оператор `goto` – все равно, что поклоняться темным силам, в Python есть более элегантные способы выхода из цикла, которые будут рассмотрены позже.

### `continue` – Пропуск итерации
Данный оператор применяется, когда в текущей итерации цикла необходимо пропустить все команды до конца тела цикла. При этом сам цикл прерываться не должен, условия продолжения или выхода должны вычисляться обычным образом.

```python
i = 0
while i < 20:
    i += 1
    if i < 5:
        continue
    elif i == 10:
        break
```

# Работа с файлами

```python
file = open('file.txt', 'w', encoding='utf8')
```
1. (абсолютный / относительный путь к файлу) + имя файла
2. режим работы
    - `r` - read (чтение)
    - `w` - write (запись)
    - `a` - append (добавление в конец)
3. кодировка символов в текстовых файлах: _`utf8`_, _`ascii`_, _`cp1251`_


```python
file = open('file.txt', 'w')  # открываем файл на запись
file.write('hello\n')  # записываем некоторое содержимое
file.close()  # закрываем файл (обязательно)

file = open('file.txt', 'r')  # открываем файл на чтение
print(file.readline())  # метод readline() читает одну строку
file.close()  # закрываем файл
```

    hello
    
    


```python
file = open('file.txt', 'a')  # открываем файл на добавление
file.write('lorem ipsum\n')  # добавляем одну строку
file.write('hello world\n')  # добавляем другую строку
file.close()  # закрываем файл (обязательно)

file = open('file.txt', 'r')  # открываем файл на чтение
line = file.read()  # метод read() читает файл полностью
file.close()  # закрываем файл (обязательно)

print(line)
```

    hello
    lorem ipsum
    hello world
    
    


```python
file = open('file.txt', 'r')
# целочисленный аргумент этого метода позволяет 
# прочитать определенное количество символов
line = file.read(10)
file.close()

print(line)
```

    hello
    lore
    

Если хочется общаться с файлом подольше, можно открыть поток работы с ним через конструкцию

```python
with open() as text:
    some_actions_w_text
```


```python
with open('lambda.txt', 'r') as text:
    for line in text:
        print(line)
```

    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
    
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
    
    in reprehenderit in voluptate velit esse cillum dolore eu fugiat
    
    nulla pariatur. Excepteur sint occaecat cupidatat non proident,
    
    sunt in culpa qui officia deserunt mollit anim id est laborum.
    
    

### task

Скачать себе файлик [`lambda.txt`](https://raw.githubusercontent.com/lambdafrela/lambda-help/master/lectures/python/lecture_2/lambda.txt), открыть в той же директории интерпретатор Python. Вывести из файла lambda.txt слова, начинающиеся с букв `a` или `u`


```python
with open('lambda.txt', 'r') as text:
    for line in text:
        for word in line.split():
            if word[0] == 'a' or word[0] == 'u':
                print(word)
            else:
                continue
```

    amet,
    adipiscing
    ut
    aliqua.
    ad
    ullamco
    ut
    aliquip
    aute
    anim
    

# Функциональное программирование

## Лямбда-выражения

Они же анонимные функции, они же "О БОЖЕ, КАК Я ЭТО МОГ НАПИСАТЬ". Удобны для определения не очень сложных функций, которые передаются затем другим функциям.

Общий вид:
```python
lambda variable_1, variable_2: expression_with_variables
```

Конструкция выше является эквивалентной обычной функции:
```python
def my_func(variable_1, variable_2):
    return expression_with_variables
```

Принцип анонимности выражается в нежелательности присваивания лямбда-выражениям именных меток. Объявил - использовал - забыл. Если функция должна применяться много раз _рекомендуется_ оформить её в классическую `def` конструкцию.


```python
# объявления лямбда-выражения с моментальным применением
(lambda x: x+2)(5)
```




    7



Для применения лямбда-функции (а также любых других функций) к элементам списка используется команда `map()`

Общий вид:
```python
map(lambda variable: expression_w_variable, iterable)
```
или, если задана функция `my_func`:
```python
map(my_func, iterable)
```

Используется, когда ваще не хочется применять цикл `for` или результатом выполнения должна стать коллекция, передающаяся дальше в другие функции.


```python
MAI = ['я','мы','лучшие люди страны']

list(map( lambda who: f'МАИ - это {who}', MAI ))
```




    ['МАИ - это я', 'МАИ - это мы', 'МАИ - это лучшие люди страны']



страшный пример из реальной жизни (пожалуйста, **никогда** не делайте так, если хотите использовать код в будущем)

```python
sigmoid = lambda y: 1. / (1 + np.exp(-y))

log_loss_from_staged_decision = lambda staged_decision, y: map(lambda pred: log_loss(y, pred), map(sigmoid, staged_decision))
    
get_train_loss = lambda lr, X, y: log_loss_from_staged_decision(get_clf(lr).staged_decision_function(X), y)

learning_rates = [1, 0.5, 0.3, 0.2, 0.1]

train_losses = map(lambda lr: get_train_loss(lr, X_train, y_train), learning_rates)

test_losses = map(lambda lr: get_train_loss(lr, X_test, y_test), learning_rates)

map(plot_graphs, train_losses, test_losses, learning_rates)
```

![y u no](https://i.ytimg.com/vi/Fr8itGELygc/hqdefault.jpg)

### task

Что делает эта строчка?

```python
data['Sex'] = data['Sex'].map(lambda x: 1 if x == 'M' else (-1 if x == 'F' else 0))
```

## Компоновки / списковые включения (Listing Comprehensions)

Наиболее выразительное из функциональных средств Python. Например, для вычисления списка квадратов положительных целых чисел, меньших 10, можно написать обычную функцию:


```python
def sqares(l):
    for x in l:
        print(x**2)

sqares(range(1, 10))
```

    1
    4
    9
    16
    25
    36
    49
    64
    81
    

а можно в одну строчку с помощью компоновок:


```python
[x**2 for x in range(1, 10)]
```




    [1, 4, 9, 16, 25, 36, 49, 64, 81]



### task

Написать ту же функцию, но с использованием лямбда-функций


```python
list(map(lambda x: x**2, range(1,10)))
```




    [1, 4, 9, 16, 25, 36, 49, 64, 81]



# ДЗ

2. [Coding Bat Lists 1](http://codingbat.com/python/List-1) - задания на списки попроще
3. [Coding Bat Lists 2](http://codingbat.com/python/List-2) - задания на списки посложнее

## в следующий раз

- исключения
- ПРАКТИЧЕСКОЕ ЗАНЯТИЕ

# референс

- [Хорошая статья про функциональное программирование с примерами](https://ru.wikipedia.org/wiki/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BD%D0%B0_Python)
- [Страшные примеры компоновок](https://en.wikipedia.org/wiki/List_comprehension)
- [Еще немного страшных примеров на русском](https://habrahabr.ru/post/30232/)
