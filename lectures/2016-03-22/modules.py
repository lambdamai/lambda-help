 #!/usr/bin/python
 # -*- coding: utf-8 -*-

""" Модули на Python """

""" Импоритируем лежащий в том же каталоге файл  test_module.py """
import test_module
print('Type of object: %s'%(str(type(test_module))) )
"""
    Теперь test_module это объект типа module, то есть модуль Python.

    Атрибуты модуля - переменные, функции и классы, объявленые в файле, доступны нам как атрибуты класса

"""
print('\nAccesing module attributes:')
test_module.func1()
test_module.func2()

print('X equals: %s'%(str(test_module.x)))
print('Y equals: %s'%(str(test_module.y)))
print('Class atr: %s'%(str(test_module.MyClass.test_atr)))

"""
Второй вариант импорта — взятие непосредственно имени без имени модуля.

Импорт на основе from обладает такой особенностью, что он делает импортируемые атрибуты read-only.

"""

from test_module import func1, func2, x
print('\nAccesing attributes with a different import:')
func1()
func2()

x = 10
print("X equals:",x)
print("Module x equals", test_module.x)


"""
В данном случае x — это локальная переменная, в то время как переменные x в модуле не меняются.

Можно задать alias ипортируемому имени для упрощения или избежания конфликта имен
"""
import test_module as md
print('\nImporting with alias')
print("Module x equals", md.x)

from test_module import func1 as f1
f1()
"""
Для выяснения имен, определенных в модуле, можно использовать встроенную функцию dir(). Она возвращает отсортированный список строк.
У модулей есть различные атрибуты, например __doc__ выведет документацию к модулю. В нашем случае это будет многострочный комментарий в начале файла. 
"""
print('\nUsing dir:')
print(dir(test_module))
with open('out.txt', "w", encoding='utf-8') as f:
    f.write(test_module.__doc__)

"""

Пакеты (packages)
Пакеты — способ структурирования пространств имен модулей на основе файловой системы. Пакетная организация дает все удобства по управлению большим количеством файлов. Пакетный импорт делает код более читабельным и значительно упрощает поиск. 
Пример:
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

Файл _init_.py необходим для того, чтобы интерпретатор распознал каталог, как содержащий пакет.
Этот файл может быть пустым. В этом файле обычно содержится информация о пакете (автор, версия, контакты и другое).

Мы можем импортировать тестовый модуль из пакета например так
"""
from test_package import package_test_module as ptm
print('\nImporting from package')
print("Module x equals", ptm.x)

""" Или так """
import test_package.package_test_module as ptm
print('\nImporting from package 2')
print("Module x equals", ptm.x)

""" Или так """
from test_package import *
print('\nImporting from package 3')
print("Module z equals", package_test_module.z)
""" Что означает импорт всех имен из пакета.

Этот вариант работает только если в __init__ файле пакета определен список __all__ , в котором перечисляются модули, которые импортируются в этом случае. 
    __all__ = ["package_test_module"]

    Источники:
        https://www.ibm.com/developerworks/ru/library/l-python_part_5/
        https://docs.python.org/3/reference/import.html
        https://docs.python.org/3/tutorial/modules.html

    Для закрепления:
        Измените любой свой (или не свой, по желанию) проект, разделив его функционал на несколько файлов.
        Например в одном файле интерфейс, в другом функционал, в третьем вспомогательные функции.

"""