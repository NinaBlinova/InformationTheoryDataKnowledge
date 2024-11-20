from collections import Counter
import numpy as np

# Исходное сообщение
text = "гладко было на бумаге, да забыли про овраги, а по ним ходить"

# Разбиваем текст на блоки по 4 символа
blocks = [text[i:i + 4] for i in range(0, len(text), 4)]
# Подсчитываем частоту появления каждого блока
block_counts = Counter(blocks)
symbols, counts = zip(*block_counts.items())

# Сортируем символы по убыванию частот для кодирования
sorted_indices = np.argsort(counts)[::-1]
symbols = [symbols[i] for i in sorted_indices]
counts = [counts[i] for i in sorted_indices]

# Функция для генерации кодов методом Шеннона-Фано с использованием 0, 1, 2 и 3
def shannon_fano(probabilities, symbols, level=0):
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
    left_codes = shannon_fano(left_probabilities, left_symbols, level + 1)
    right_codes = shannon_fano(right_probabilities, right_symbols, level + 1)

    # Используем 0, 1, 2, 3 для кодов, меняя порядок на каждом уровне рекурсии
    for i, (symbol, code) in enumerate(left_codes.items()):
        codes[symbol] = str((level + i) % 4) + code  # Циклически используем 0-3 для левой группы
    for i, (symbol, code) in enumerate(right_codes.items()):
        codes[symbol] = str((level + i + 2) % 4) + code  # Смещение для правой группы

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
    encoded_message = ''.join(codes.get(text[i:i + 4], '') for i in range(0, len(text), 4))  # Кодируем блоки по 4 символа
    return encoded_message

# Кодируем сообщение
encoded_message = encode_message(text, codes)
print(f'Закодированное сообщение: {encoded_message}')

# Вывод всех кодов символов
print("\nКоды символов:")
for symbol, code in codes.items():
    print(f'{symbol}: {code}')

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
    return average_length / k + 1

# Вычисляем среднее число сигналов на 4-буквенную комбинацию
k = 4
average_signals = average_signals_per_k(codes, k)
print(f'\nСреднее число элементарных сигналов на одну {k}-буквенную комбинацию: {average_signals:.2f}')
