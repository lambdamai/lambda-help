"""Демонстрационный модуль python"""

class MyClass():
	test_atr = "Lambda"

def func1():
	print('Func 1')

def func2():
	print('Func 2')

x = 1
y = 2


if __name__ == "__main__":
	print('test module has been ran independently')
else:
	print('test module has been imported')