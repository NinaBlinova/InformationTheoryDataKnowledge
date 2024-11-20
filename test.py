import sys
from collections import Counter
import math


# Разделение текста на блоки длины k
def split_text_into_blocks(text, k):
    return [text[i:i + k] for i in range(0, len(text), k)]


# Построение дерева Шеннона-Фано
def shannon_fano(symbols, prefix=''):
    if len(symbols) == 1:
        return {symbols[0][0]: prefix}
    # Находим точку разделения списка символов
    total = sum([freq for _, freq in symbols])
    acc = [0] * 3
    i1, i2, i3 = 0, 0, 0
    for i in range(len(symbols)):
        x = symbols[i][1]
        acc[0] += x
        if acc[0] >= total / 4:
            i1 = i + 1
            break
        if i1 > 0 and i > i1:
            acc[1] += x
            if acc[1] >= total / 4:
                i2 = i + 1
                break
        if i2 > 0 and i > i2:
            acc[2] += x
            if acc[2] >= total / 4:
                i3 = i + 1
                break

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


# Основная функция
def main():
    text = "Гладко было на бумаге, да забыли про овраги, а по ним ходить."

    k = 4

    # Частотный анализ символов
    counter = Counter(text)
    total_chars = sum(counter.values())
    symbols = [(char, freq / total_chars) for char, freq in counter.items()]

    # Сортируем символы по вероятности в порядке убывания
    symbols = sorted(symbols, key=lambda x: x[1], reverse=True)

    # Строим коды Шеннона-Фано
    codes = shannon_fano(symbols)

    # Вывод результатов
    print("Символы и их коды Шеннона-Фано:")
    for char, code in codes.items():
        print(f"{char}: {code}")

if __name__ == "__main__":
    main()
