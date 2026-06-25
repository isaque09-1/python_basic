import time


def fazer_arroz():
    print('Fazendo arroz...')
    time.sleep(3) # I/O - bloqueia o código
    print('Arroz pronto!')


def fazer_carne():
    print('Fazendo carne...')
    time.sleep(5) # I/O - bloqueia o código
    print('Carne pronta!')


def fazer_feijao():
    print('Fazendo feijão...')
    time.sleep(7) # I/O - bloqueia o código
    print('Feijão pronto!')


def cozinhar():
    fazer_arroz()
    fazer_carne()
    fazer_feijao()
    print('Almoço pronto!')


cozinhar()