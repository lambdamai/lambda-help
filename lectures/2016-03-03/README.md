
# Регулярные выражения в Python

## Теория:

Регулярные выражения - формальный язык для поиска и манипуляций текстом, в частности подстроками.

Регулярные выражения основаны на масках (pattern). Это шаблоны или правила, которые удовлетворяют некоторому множеству строк.
Так, из простых примеров, можно найти все вхождения "кот" в строку "кот терракот котом котором".

Плюсы:
+ удобны в использовании
+ универсальны

Минусы:
- регулярные выражения для сложных задач (с множеством условий) нечитабельны и сложны в разработке
- регулярные выражения работают медленно


В Python регулярные выражения предоставляются библиотекой "re". Она изначально установлена для всех официальных сборок Python.

Рассмотрим самые часто используемые методы:
- `re.match()`
- `re.search()`
- `re.findall()`
- `re.split()`
- `re.sub()`
- `re.compile()`




```python
import re

# Текст, над которым мы будем проводить операции с помощью регулярных выражений
text = "The object has the words \"NO STEP\" on it and could be from the plane's horizontal stabilizer - \
        the wing-like parts attached to the tail, sources say. It was discovered by an American who has been \
        blogging about the search for MH370."

print("Text for searching:\n%s\n" % (text))
```

    Text for searching:
    The object has the words "NO STEP" on it and could be from the plane's horizontal stabilizer - the wing-like parts attached to the tail, sources say. It was discovered by an American who has been blogging about the search for MH370.
    
    

Рассмотрим методны на простом примере: поиске полного соответствия

```python
re.match(pattern, string)
``` 
ищет подходящую под маску pattern строку в начале строки text.



```python
pattern = r'The'  # r перед строкой указывает, что это "raw string" для регулярного выражения

# Почему так см.
# https://docs.python.org/3/howto/regex.html#the-backslash-plague

result = re.match(pattern, text)
# При успешном поиске будет создан особый объект с результатом, при неуспешном в result запишется None, то есть ничего.
# Если попытаться вывести result - возникнет ошибка

# Если найдено, вывести найденный текст, если нет, вывести, что не найдено.
result = result.group(0) if result else "Not found"
# используем метод .group(0) чтобы указать, что хотим получить результат
# первой группы. О группах позже
print("Searching for \"%s\" using match.\nResult:\n%s\n" %
      (str(pattern), str(result)))
```

    Searching for "The" using match.
    Result:
    The
    
    

Попробуем использовать match для поиска второго слова

Напишем вспомогательную функцию


```python
def result_or_not_found(result):
    return result.group(0) if result else "Not found"

pattern = r'object'
result = result_or_not_found(re.match(pattern, text))
print("Searching for \"%s\" using match.\nResult:\n%s\n" %
      (str(pattern), str(result)))
```

    Searching for "object" using match.
    Result:
    Not found
    
    

`re.search(pattern, string)` похож на `match()`, но он ищет не только в начале строки

Повторим опыт с помощью `search`


```python
pattern = r'The'
result = result_or_not_found(re.search(pattern, text))
print("Searching for \"%s\" using search.\nResult:\n%s\n" %
      (str(pattern), str(result)))
```

    Searching for "The" using search.
    Result:
    The
    
    

Попробуем использовать search для поиска второго слова


```python
pattern = r'object'
result = result_or_not_found(re.search(pattern, text))
print("Searching for \"%s\" using search.\nResult:\n%s\n" %
      (str(pattern), str(result)))
```

    Searching for "object" using search.
    Result:
    object
    
    

В отличие от match мы получили искомую строку.

-----

`re.findall(pattern, string)` возвращает список всех найденных совпадений


```python
pattern = r'the'
result = re.findall(pattern, text)
print("Searching for \"%s\" using findall.\nResult:\n%s\n" %
      (str(pattern), str(result)))
```

    Searching for "the" using findall.
    Result:
    ['the', 'the', 'the', 'the', 'the']
    
    

`re.split(pattern, string, [maxsplit=0])` делит строку по маске
`maxsplit` определяет максимальное количество разделений. При 0 метод разделит строку столько раз, сколько возможно.


```python
pattern = r'the'
result = re.split(pattern, text)
print("Splitting text by \"%s\" using split.\nResult:\n%s\n" %
      (str(pattern), str(result)))
```

    Splitting text by "the" using split.
    Result:
    ['The object has ', ' words "NO STEP" on it and could be from ', " plane's horizontal stabilizer - ", ' wing-like parts attached to ', ' tail, sources say. It was discovered by an American who has been blogging about ', ' search for MH370.']
    
    

`re.sub(pattern, repl, string)` ищет маску `pattern` в строке `string` и заменяет её на строку `repl`


```python
pattern = r'NO STEP'
repl = 'LAMBDA'
result = re.sub(pattern, repl, text)
print("Replacing \"%s\" by \"%s\" using sub.\nResult:\n%s\n" %
      (str(pattern), str(repl), str(result)))
```

    Replacing "NO STEP" by "LAMBDA" using sub.
    Result:
    The object has the words "LAMBDA" on it and could be from the plane's horizontal stabilizer - the wing-like parts attached to the tail, sources say. It was discovered by an American who has been blogging about the search for MH370.
    
    

`re.compile()` создает из строки отдельный объект, который мы можем использовать для дальнейших операций.
Компиляция паттерна регулярного выражения ускоряет поиск.


```python
pattern = re.compile(r'the')
result = pattern.findall(text)
print("Searching for \"%s\" using findall with compiled str in text1.\nResult:\n%s\n" %
      (str(pattern), str(result)))
```

    Searching for "re.compile('the')" using findall with compiled str in text1.
    Result:
    ['the', 'the', 'the', 'the', 'the']
    
    


```python
text2 = "Early photographic analysis of the object suggests it could have come from the doomed jet,\
         which vanished almost exactly 2 years ago."
result = pattern.findall(text2)  # Не нужно компилировать паттерн заново
print("Searching for \"%s\" using findall with compiled str in text2.\nResult:\n%s\n" %
      (str(pattern), str(result)))
```

    Searching for "re.compile('the')" using findall with compiled str in text2.
    Result:
    ['the', 'the']
    
    

Пока что в наших паттернах использовались только обычные символы.

"The" соответствует на языке регулярных выражений только строке "The".

Посмотрим на мощный инструмент: метасимволы.
Метасимволы это символы, которые соответстуют особым шаблонам. Вот они.

- `.`   Один любой символ, кроме новой строки `\n`.
- `?`   0 или 1 вхождение шаблона слева
- `+`   1 и более вхождений шаблона слева
- `*`   0 и более вхождений шаблона слева
- `\w`  Любая цифра или буква (`\W` — все, кроме буквы или цифры)
- `\d`  Любая цифра `[0-9]` (`\D` — все, кроме цифры)
- `\s`  Любой пробельный символ (`\S` — любой непробельнй символ)
- `\b`  Граница слова
- `[..]`    Один из символов в скобках (`[^..]` — любой символ, кроме тех, что в скобках)
- `\`   Экранирование специальных символов (`\.` означает точку или `\+` — знак «плюс»)
- `^` и `$`   Начало и конец строки соответственно
- `{n,m}`   От `n` до `m` вхождений (`{,m}` — от `0` до `m`)
- `a|b` Соответствует `a` или `b`
- `()`  Группирует выражение и возвращает найденный текст
- `\t`, `\n`, `\r`  Символ табуляции, новой строки и возврата каретки соответственно

-----

Примеры использования:


```python
all_symbols = r'*'  # Соответствует всей строе
# соответстует одному символу, findall с этим паттерном вернет список
# символов в строке
symbols = r'.'
# соответстует одной букве или цифре, findall с этим паттерном вернет
# список символов в строке за исключением пробелов
letters_and_numbers = r'\w'
# findall с этим паттерном вернет список цифр найденных в строке
number = r'\d'
# findall с этим паттерном вернет список a и an найденных в строке
articules = r'a|an'
# findall с этим паттерном вернет список со всеми точками в строке.
# Заметьте что из-за экранирования паттерн не соответствует никаким
# символам, кроме точи
dots = r'\.'
# findall с этим паттерном вернет список с последним словом в строке
last_word = r'\w*\.$'
all_words = r'\w+'  # findall с этим паттерном вернет список слов
# findall с этим паттерном вернет слова, заключенные в кавычки
quoted = r'\".*\"'

# findall с этим паттерном вернет слова с 5 или более буквами
longwords = r'\w{5,}'

# findall с этим паттерном вернет первые 3 буквы каждого слова
first_three_letters = r'\b\w{3}'

# findall с этим паттерном вернет слова начинающиеся на a, b или с
starting_with = r'\b[abc]\w+'

# findall с этим паттерном вернет слова не начинающиеся на a, b или с.
# Обратите внимание на пробел в скобках: он означает, что мы не ищем
# последовательности символов начинающиеся с пробела.
starting_not_with = r'\b[^abc ]\w+'
```

### Проверка телефонного номера


```python
li = ['9999999999', '999999-999', '99999x9999', '892512303', '89293536800']
for val in li:
    if re.match(r'[8-9]{1}[0-9]{9}', val) and len(val) == 10:
        print(True)
    else:
        print(False)
```

    True
    False
    False
    False
    False
    

## Источники и дальнейшее чтение:

http://tproger.ru/translations/regular-expression-python/
https://habrahabr.ru/post/115825/

http://pep8.ru/doc/dive-into-python-3/7.html

https://docs.python.org/3/howto/regex.html


Для закрепления знаний:
    Напишите программу, которая позволяет пользователю ввести с клавиатуры email и пароль. Проверьте их на следующие правила:

        email:
            содержит только латинские буквы, цифры, @ и точку 
            содержит @ и домен и зону (.ru, .com и прочее)
            домен не короче 3 символов, не длиннее 10 символов, не начинается с цифры
            доменная зона не короче двух символов, не имеет цифр
            имя пользователя не длиннее 10 символов, не начинается с цифры

        пароль:
            длиннее трех, короче четырех
            содержит любые символы кроме пробела, таба и переноса строки
            содержит хотя бы одну латинскую букву, одну цифру, одну латинскую букву верхнего регистра
            не содержит последовательностей букв длиннее трех символов

    Вам не обязетельно реализовывать все правила в одном регулярном выражении. Вы можете поступать как удобно, главное чтобы это работало корректно и вы сами могли понять то, что написали.
