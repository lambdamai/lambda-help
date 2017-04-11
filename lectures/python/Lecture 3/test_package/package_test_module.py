"""Демонстрационный модуль python"""

class MyClass():
	test_atr = "Lambda"

def func1():
	print('Package Func 1')

def func2():
	print('Package Func 2')

x = 100
y = 200

z = 300



if __name__ == "__main__":
	print('test module has been ran independently')
else:
	print('test module has been imported')