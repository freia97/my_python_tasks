from Person import *

tom = Person("Tom")

tom.display_info()  # Имя: Tom  Возраст: 1
tom.set_age(-3486)  # Недопустимый возраст
tom.set_age(25)
tom.display_info()