# Построение дерева Шеннона-Фано
import sys


def shannon_fano(symbols, prefix=''):
    if len(symbols) == 1:
        return {symbols[0][0]: prefix}

    # Сортируем символы по вероятности в порядке убывания
    symbols = sorted(symbols, key=lambda x: x[1], reverse=True)

    # Находим точку разделения списка символов
    total = sum([freq for _, freq in symbols])
    acc = [0] * 3
    i1, i2, i3 = 0, 0, 0
    mn1, mn2, mn3 = sys.maxsize, sys.maxsize, sys.maxsize
    for i in range(len(symbols)):
        x = symbols[i][1]
        acc[0] += x
        if mn1 > abs(total - acc[0] * 4):
            mn1 = abs(total - acc[0] * 4)
            i1 = i + 1
        if i1 > 0 and i > i1:
            acc[1] += x
            if mn2 > abs(total - acc[1] * 4):
                mn2 = abs(total - acc[1] * 4)
                i2 = i + 1
        if i2 > 0 and i > i2:
            acc[2] += x
            if mn3 > abs(total - acc[2] * 4):
                mn3 = abs(total - acc[2] * 4)
                i3 = i + 1

    # Рекурсивно делим на две части и назначаем 0, 1, 2, 3
    part1 = shannon_fano(symbols[:i1], prefix + '0')
    part2 = shannon_fano(symbols[i1:i2], prefix + '1')
    part3 = shannon_fano(symbols[i2:i3], prefix + '2')
    part4 = shannon_fano(symbols[i3:], prefix + '3')

    # Объединяем результаты
    part1.update(part2)
    part1.update(part3)
    part1.update(part4)
    return part1