import logging
import random


while True:
    # устанавливаем уровень логирования
    logging.basicConfig(filename="ex.log", level=logging.INFO)
    logging.info("Programm started")
    # запрашиваем у пользователя количество бочек
    try:
        N = int(input("Введите количество бочек: "))
        if N < 1:
            logging.warning("Количество бочек должно быть не меньше 1")
            continue
        break
    except ValueError:
        logging.warning("Вы ввели не число. Пожалуйста, введите целое число")

# создаем список из N элементов, нумеруемых от 1 до N
bag = list(range(1, N+1))

while len(bag) > 0:
    # запрашиваем у пользователя нажатие кнопки
    input("Нажмите Enter, чтобы вытащить бочонок")
    # выбираем случайный бочонок из мешка
    draw = random.choice(bag)
    print("Вытянут бочонок номер", draw)
    logging.info("number %d", draw)
    # убираем бочонок из мешка
    bag.remove(draw)
    logging.info("Programms end")