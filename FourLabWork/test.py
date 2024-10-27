# Исходный текст
from numpy import sort

text = "гладко было на бумаге, да забыли про овраги, а по ним ходить"

frequency_dict = {
    " ": 0.15,
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


# Разделение текста на блоки длины k
def split_text_into_blocks(text, k):
    return [text[i:i + k] for i in range(0, len(text), k)]


def find_probability(blocks, frequency_dict, k):
    block_probability = {}
    for block in blocks:
        probability = 1.0
        for i in range(0, k):
            prob = frequency_dict.get(block[i].lower(), 0)
            probability *= prob
        block_probability[block] = probability
    return block_probability


# Основная логика программы
block_size = 4
blocks = split_text_into_blocks(text, block_size)
print(blocks)

probabilities = find_probability(blocks, frequency_dict, block_size)
sorted_prob = dict(sorted(probabilities.items()))
# Вывод результатов
for b, p in sorted_prob.items() :
    print(f"Блок: '{b}' - Вероятность: {p:.10f}")

