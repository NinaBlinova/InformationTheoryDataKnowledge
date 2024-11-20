# Исходное сообщение
from collections import Counter

import numpy as np

text = "Нина и Вова Блиновы"
# text = "гладко было на бумаге, да забыли про овраги, а по ним ходить"

blocks = [text[i:i + 4] for i in range(0, len(text), 4)]
# Подсчитываем частоту появления каждого блока
block_counts = Counter(blocks)
symbols, counts = zip(*block_counts.items())

# Сортируем символы по убыванию частот для кодирования
sorted_indices = np.argsort(counts)[::-1]
symbols = [symbols[i] for i in sorted_indices]
counts = [counts[i] for i in sorted_indices]


# Функция для генерации кодов методом Шеннона-Фано
def shannon_fano(probabilities, symbols):
    if len(probabilities) == 1:
        return {symbols[0]: ''}

    cumulative_probabilities = [sum(probabilities[:i + 1]) for i in range(len(probabilities))]
    total = cumulative_probabilities[-1]
    half = total / 2
    split_index = next(i for i in range(len(cumulative_probabilities)) if cumulative_probabilities[i] >= half) + 1

    left_symbols = symbols[:split_index]
    right_symbols = symbols[split_index:]
    left_probabilities = probabilities[:split_index]
    right_probabilities = probabilities[split_index:]

    codes = {}
    left_codes = shannon_fano(left_probabilities, left_symbols)
    right_codes = shannon_fano(right_probabilities, right_symbols)

    for symbol, code in left_codes.items():
        codes[symbol] = '0' + code  # Используем '0'
    for symbol, code in right_codes.items():
        codes[symbol] = '1' + code  # Используем '1'

    # Корректируем коды для четверичной системы
    # Используем '2' и '3' для дальнейшего деления
    for i, (symbol, code) in enumerate(codes.items()):
        if i % 4 == 2:
            codes[symbol] = '2' + code
        elif i % 4 == 3:
            codes[symbol] = '3' + code

    return codes


# Генерируем коды
codes = shannon_fano(counts, symbols)


# Проверка уникальности кодов
def check_unique_codes(codes):
    code_set = set(codes.values())
    return len(code_set) == len(codes)


if not check_unique_codes(codes):
    print("Обнаружены неуникальные коды!")
else:
    print("Все коды уникальны.")


# Функция для кодирования сообщения
def encode_message(text, codes):
    encoded_message = ''.join(
        codes.get(text[i:i + 4], '') for i in range(0, len(text), 4))  # Кодируем блоки по 4 символа
    return encoded_message


# Кодируем сообщение
encoded_message = encode_message(text, codes)
print(f'Закодированное сообщение: {encoded_message}')

# Вывод всех кодов символов
print("\nКоды символов:")
for symbol, code in codes.items():
    print(f'{symbol}: {code}')


# ДА
# Функция для декодирования сообщения
def decode_message(encoded_message, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ''
    decoded_message = ''

    for bit in encoded_message:
        current_code += bit
        if current_code in reverse_codes:
            decoded_message += reverse_codes[current_code]
            current_code = ''

    return decoded_message


# Декодируем сообщение
decoded_message = decode_message(encoded_message, codes)
print(f'\nДекодированное сообщение: {decoded_message}')


# Функция для вычисления среднего числа сигналов
def average_signals_per_k(codes, k):
    total_length = sum(len(code) for code in codes.values())
    average_length = total_length / len(codes)
    return average_length / k


# Вычисляем среднее число сигналов на 4-буквенную комбинацию
k = 4
average_signals = average_signals_per_k(codes, k)
print(f'\nСреднее число элементарных сигналов на одну {k}-буквенную комбинацию: {average_signals:.2f}')
