from collections import Counter
import math

# Исходный текст
text = "Глaдкo былo нa бyмaгe, дa зaбыли прo oврaги, a пo ним xoдить"

frequency_dict = {
    ' ': 0.15,
    ',': 0.1,
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
    'ё': 0.00013
}


# Функция для разбивки текста на блоки заданной длины
def split_into_blocks(text, block_size):
    return [text[i:i + block_size] for i in range(0, len(text), block_size)]


# Функция для вычисления вероятностей блоков
def calculate_probabilities(blocks):
    probabilities = 1

    return probabilities


# Функция для кодирования методом Шеннона-Фано
def shannon_fano_coding(probabilities):
    sorted_blocks = sorted(probabilities.items(), key=lambda item: item[1], reverse=True)
    codes = {}

    def assign_codes(blocks):
        if len(blocks) == 1:
            codes[blocks[0][0]] = ""
            return

        total = sum(prob for _, prob in blocks)
        cumulative = 0
        split_index = 0

        for i, (block, prob) in enumerate(blocks):
            cumulative += prob
            if cumulative >= total / 2:
                split_index = i + 1
                break

        assign_codes(blocks[:split_index])
        assign_codes(blocks[split_index:])

        for i in range(split_index):
            codes[blocks[i][0]] = '0' + codes[blocks[i][0]]
        for i in range(split_index, len(blocks)):
            codes[blocks[i][0]] = '1' + codes[blocks[i][0]]

    assign_codes(sorted_blocks)
    return codes


# Функция для вычисления среднего числа сигналов
def average_signal_length(codes, probabilities):
    return sum(len(codes[block]) * prob for block, prob in probabilities.items())


# Основная логика программы
block_size = 4
blocks = split_into_blocks(text, block_size)
probabilities = calculate_probabilities(blocks)
codes = shannon_fano_coding(probabilities)
avg_length = average_signal_length(codes, probabilities)

# Вывод результатов
print("Блоки:")
print(blocks)
print("nВероятности:")
for block, prob in probabilities.items():
    print(f"{block}: {prob:.4f}")
print("nКоды:")
for block, code in codes.items():
    print(f"{block}: {code}")
print(f"nСреднее число элементарных сигналов: {avg_length:.4f}")
