from singleton import Singleton


x = Singleton.get_instance()
y = Singleton.get_instance()

print(x, y)
