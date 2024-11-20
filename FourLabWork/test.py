import sys
from itertools import product

text = "гладко было на бумаге, да забыли про овраги, а по ним ходить"

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
    'ё': 0.00013
}


def probability(dict, k):
    block_probability = {}

    # Генерируем все возможные сочетания букв длиной k
    for combination in product(dict.keys(), repeat=k):
        # Вычисляем вероятность для текущей комбинации
        prob = 1
        for letter in combination:
            prob *= dict[letter]
        # Преобразуем кортеж в строку для удобства
        block = ''.join(combination)
        block_probability[block] = prob

    return block_probability


tree = dict(sorted(probability(frequency_dict, 4).items(), key=lambda item: item[1], reverse=True))
keysList = list(tree.keys())
p = list(tree.values())


def divide(mpDivide):
    allSum = 0
    for i in range(len(mpDivide)):
        allSum += mpDivide[i]
    i1, i2, i3, mn1, mn2, mn3 = 0, 0, 0, sys.maxsize, sys.maxsize, sys.maxsize
    sums = [0, 0, 0]
    for k in range(len(mpDivide)):
        x = mpDivide[k]
        sums[0] += x
        if mn1 > abs(allSum - sums[0] * 4):
            mn1 = abs(allSum - sums[0] * 4)
            i1 = k + 1
        if i1 > 0 and k > i1:
            sums[1] += x
            if mn2 > abs(allSum - sums[1] * 4):
                mn2 = abs(allSum - sums[1] * 4)
                i2 = k + 1
        if i2 > 0 and k > i2:
            sums[2] += x
            if mn3 > abs(allSum - sums[2] * 4):
                mn3 = abs(allSum - sums[2] * 4)
                i3 = k + 1
    return mpDivide[:i1], mpDivide[i1:i2], mpDivide[i2:i3], mpDivide[i3:]


# iterable_object[start:stop:step]
# s1, s2, s3, s4 = divide(p)
# print(sum(s1), len(s1), sum(s2), len(s2))
# print(sum(s3), len(s3), sum(s4), len(s4))


def label(mpLabel):  # to denote the right side with 1, left side with 0
    dictSF = {}
    if len(mpLabel) > 1:
        mp1, mp2, mp3, mp4 = divide(mpLabel)
        for i in range(len(mp1)):
            dictSF[mp1[i]] = dictSF.get(mp1[i], '') + '0'
        for i in range(len(mp2)):
            dictSF[mp2[i]] = dictSF.get(mp2[i], '') + '1'
        for i in range(len(mp3)):
            dictSF[mp3[i]] = dictSF.get(mp3[i], '') + '2'
        for i in range(len(mp4)):
            dictSF[mp4[i]] = dictSF.get(mp4[i], '') + '3'

        # Рекурсивные вызовы
        dictSF.update(label(mp1))
        dictSF.update(label(mp2))
        dictSF.update(label(mp3))
        dictSF.update(label(mp4))

    # Если длины всех подмассивов равны 1, просто возвращаем текущий словарь
    return dictSF


d = label(p)
print(d)
