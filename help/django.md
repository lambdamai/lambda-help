# Установка Django

Давай установим Django, используя `pip`. Для этого, в командной строке надо выполнить команду `pip install django==1.9` (конкретная версия указывается для того, чтобы совместная работа над проектом велась на одной и той же версии фреймворка)

```
> pip install django==1.9
Downloading/unpacking django==1.9
Installing collected packages: django
Successfully installed django
Cleaning up...
```

Для того, чтобы проверить, установился ли Django, откроем в командной строке Python:
```
> python
```
и выполним следующие команды:
```python
import django
print(django.get_version())
```
результатом этих действий должна стать строчка, содержащая версию установленного пакета:
```
1.9
```