from collections import Counter
import math


# Разделение текста на блоки длины k
def split_text_into_blocks(text, k):
    return [text[i:i + k] for i in range(0, len(text), k)]


# Построение дерева Шеннона-Фано
def shannon_fano(symbols, prefix=''):
    if len(symbols) == 1:
        return {symbols[0][0]: prefix}

    # Сортируем символы по вероятности в порядке убывания
    symbols = sorted(symbols, key=lambda x: x[1], reverse=True)

    # Находим точку разделения списка символов
    total = sum([freq for _, freq in symbols])
    acc = 0
    split_index = 0
    for i, (_, freq) in enumerate(symbols):
        acc += freq
        if acc >= total / 2:
            split_index = i + 1
            break

    # Рекурсивно делим на две части и назначаем 0 и 1
    left_part = shannon_fano(symbols[:split_index], prefix + '0')
    right_part = shannon_fano(symbols[split_index:], prefix + '1')

    # Объединяем результаты
    left_part.update(right_part)
    return left_part


# Кодирование текста с помощью кодов Шеннона-Фано
def encode_text(text, codes):
    return ''.join([codes[char] for char in text])


# Декодирование текста с помощью кодов Шеннона-Фано
def decode_text(encoded_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    decoded_text = ''
    current_code = ''
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ''
    return decoded_text


# Основная функция
def main():
    text = "Гладко было на бумаге, да забыли про овраги, а по ним ходить."
    k = 4

    # Разделяем текст на блоки длины k
    blocks = split_text_into_blocks(text, k)

    # Частотный анализ символов
    counter = Counter(text)
    total_chars = sum(counter.values())
    symbols = [(char, freq / total_chars) for char, freq in counter.items()]

    # Строим коды Шеннона-Фано
    codes = shannon_fano(symbols)

    # Кодируем текст
    encoded_text = encode_text(text, codes)

    # Декодируем текст
    decoded_text = decode_text(encoded_text, codes)

    # Считаем количество элементарных символов в коде
    num_elementary_symbols = len(encoded_text)
    num_blocks = len(blocks)
    avg_elementary_symbols_per_block = num_elementary_symbols / num_blocks

    # Вывод результатов
    print("Символы и их коды Шеннона-Фано:")
    for char, code in codes.items():
        print(f"{char}: {code}")
    print(f"\nЗакодированный текст: {encoded_text}")
    print(f"Декодированный текст: {decoded_text}")
    print(f"Среднее число элементарных сигналов на одну {k}-буквенную комбинацию: {avg_elementary_symbols_per_block}")


if __name__ == "__main__":
    main()
