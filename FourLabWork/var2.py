# Исходное сообщение
text = "гладко было на бумаге, да забыли про овраги, а по ним ходить"

# Вероятности символов
frequency_dict = {
    'о': 0.10983,
    'е': 0.08483,
    'а': 0.07998,
    'и': 0.07367,
    'н': 0.06700,
    'т': 0.06318,
    'с': 0.05473,
    'р': 0.04746,
    'в': 0.04533,
    'л': 0.04343,
    'к': 0.03486,
    'м': 0.03203,
    'д': 0.02977,
    'п': 0.02804,
    'у': 0.02615,
    'я': 0.02001,
    'ы': 0.01898,
    'ь': 0.01735,
    'г': 0.01687,
    'з': 0.01641,
    'б': 0.01592,
    'ч': 0.01450,
    'й': 0.01208,
    'х': 0.00966,
    'ж': 0.00940,
    'ш': 0.00718,
    'ю': 0.00639,
    'ц': 0.00486,
    'щ': 0.00361,
    'э': 0.00331,
    'ф': 0.00267,
    'ъ': 0.00037,
    'ё': 0.00013,
    ',': 0.02,
    ' ': 0.1
}




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

    # Используем 0, 1, 2, 3 для кодов
    for i, (symbol, code) in enumerate(left_codes.items()):
        codes[symbol] = str(i % 2) + code  # Используем '0' и '1' для левой группы
    for i, (symbol, code) in enumerate(right_codes.items()):
        codes[symbol] = str(i % 2 + 2) + code  # Используем '2' и '3' для правой группы

    return codes


# Получаем список символов и их вероятностей
symbols = list(frequency_dict.keys())
probabilities = list(frequency_dict.values())

# Сортируем вероятности и символы
sorted_symbols_probabilities = sorted(zip(probabilities, symbols), reverse=True)
sorted_probabilities, sorted_symbols = zip(*sorted_symbols_probabilities)

# Генерируем коды
codes = shannon_fano(sorted_probabilities, sorted_symbols)


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
    encoded_message = ''.join(codes.get(char, '') for char in text)  # Кодируем все символы, включая пробелы и запятые
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
    return average_length / k


# Вычисляем среднее число сигналов на 4-буквенную комбинацию
k = 4
average_signals = average_signals_per_k(codes, k)
print(f'\nСреднее число элементарных сигналов на одну {k}-буквенную комбинацию: {average_signals:.2f}')
