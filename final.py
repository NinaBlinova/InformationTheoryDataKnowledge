import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *

# Заданные значения
x_values = np.array([-2, -1, 0, 1, 2, 3, 4])
p_values = np.array([0.05, 0.1, 0.18, 0.25, 0.2, 0.12])

# Вычисляем недостающее значение вероятности
missing_probability = round(1 - np.sum(p_values), 2)

# Добавляем недостающее значение в массив вероятностей
p_values = np.append(p_values, missing_probability)


def theCmulativeDistributionFunction(x_value, p_values):
    # Проверка, чтобы сумма вероятностей равнялась 1
    if sum(p_values) < 1:
        p_values.append(1 - sum(p_values))  # Добавляем недостающее значение
    # Вычисляем функцию распределения и округляем до двух знаков
    F = np.round(np.cumsum(p_values), 2)
    return F



def mathematicalExpectation(x, p):
    step1 = [x[i] * p[i] for i in range(len(p))]
    mo = sum(step1)
    return mo


# print(mathematicalExpectation(x_values, p_values))
# 1.21


def moda(x, p):
    index_max_p = 0
    for i in range(len(p)):
        if p[i] >= p[i - 1]:
            index_max_p = i
    return x[index_max_p]


# print(moda(x_values, p_values))
# 1

def median(F, x):
    # Находим индексы, где F(x) равно 0.5
    imed = np.where(F == 0.5)[0]

    if imed.size == 0:  # Если нет таких точек
        imed = np.min(np.where(F > 0.5)[0])  # Номер точки разрыва через 0.5
        medx = x[imed]  # Медиана
    else:  # Если такие точки есть
        medx = np.mean(x[imed[0]:imed[0] + 2])  # Середина отрезка с F(x)=0.5

    # print(f'Медиана = {medx:.2f}.')
    return medx


# print(median(theCmulativeDistributionFunction(x_values, p_values), x_values))
# 1

def initialMoment(x, p, m):
    alpham = [x[i] ** m * p[i] for i in range(len(p))]
    return sum(alpham)


# print(initialMoment(x_values, p_values, 2))

def centralMoment(x, p, m):
    Mm = [(x[i] - mathematicalExpectation(x_values, p_values)) ** m * p[i] for i in range(len(p))]
    return round(sum(Mm), 1)


# print(centralMoment(x_values, p_values, 1))


def clicked_btn1():
    # Создаем DataFrame для отображения таблицы
    data = {'x': x_values, 'p(x)': p_values}
    df = pd.DataFrame(data)

    # Настройка графика
    plt.figure(figsize=(10, 6))

    # Строим многоугольник распределения
    plt.plot(x_values, p_values, marker='o', linestyle='-', color='b', label='Многоугольник распределения')
    plt.fill_between(x_values, p_values, alpha=0.2)

    # Настройки графика
    plt.title('Многоугольник распределения дискретной случайной величины')
    plt.xlabel('Значения X')
    plt.ylabel('Вероятности P(X)')
    plt.xticks(x_values)
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()

    # Отображаем таблицу рядом с графиком
    plt.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='right', bbox=[1.05, 0.1, 0.4, 0.8])

    # Показываем график
    plt.tight_layout()
    plt.show()


def clicked_btn2():
    F = theCmulativeDistributionFunction(x_values, p_values)
    # Подготавливаем данные для графика
    x1 = np.concatenate(([x_values[0] - 0.5], x_values, [x_values[-1] + 0.5]))
    F1 = np.concatenate(([0], F, [1]))

    # Вычисляем промежутки
    intervals = [f"{x_values[i]}-{x_values[i + 1]}" for i in range(len(x_values) - 1)]

    # Создаем график
    plt.figure(figsize=(10, 6))
    plt.step(x1, F1, where='post', color='k', label='Функция распределения')
    plt.scatter(x_values, F, color='k')  # Изменено на F вместо F[:-1]

    # Добавляем стрелки для обозначения значений функции распределения
    for i in range(len(F)):
        xi = [x1[2 + i], x1[2 + i]]  # координаты стрелок
        Fi = [F[i], F[i]]
        plt.annotate('', xy=(xi[0], Fi[0]), xytext=(xi[0], 0),
                     arrowprops=dict(arrowstyle='->', color='black'))

    # Настройки графика
    plt.xlim(min(x1), max(x1))
    plt.ylim(0, 1)
    plt.title('Функция распределения', fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('F(x)', fontsize=12)
    plt.grid()
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # Создаем DataFrame для отображения таблицы
    data = {'Интервал': intervals, 'F': F[:-1]}  # Убираем последнее значение вероятности
    table_data = np.array(list(zip(intervals, F[:-1])))

    # Добавляем таблицу рядом с графиком
    plt.table(cellText=table_data,
              colLabels=['Интервал', 'F'],
              cellLoc='center',
              loc='right',
              bbox=[1.05, 0.1, 0.4, 0.8])

    # Показываем график
    plt.legend()
    plt.tight_layout()
    plt.show()


def clicked_btn3():
    # Вычисление необходимых значений
    mo = mathematicalExpectation(x_values, p_values)
    mode = moda(x_values, p_values)
    F = theCmulativeDistributionFunction(x_values, p_values)  # Функция распределения
    med = median(F, x_values)
    sko = round(centralMoment(x_values, p_values, 2) ** 0.5, 2)
    ax = centralMoment(x_values, p_values, 3) / (sko ** 3)
    ex = centralMoment(x_values, p_values, 4) / (sko ** 4) - 3
    print('Начальные моменты')
    for i in range(1, 5):
        initial_mom = initialMoment(x_values, p_values, i)
        print(f'Начальный момент {i} : {initial_mom}')
        print('--------')
    print('Центральные моменты')
    for i in range(1, 5):
        centlal_mom = centralMoment(x_values, p_values, i)
        print(f'Центральный момент {i} : {centlal_mom}')
        print('--------')

    # Отображение результатов
    print(f'Математическое ожидание: {mo:.2f}')
    print(f'Мода: {mode}')
    print(f'Медиана: {med:.2f}')
    print(f'Дисперсия = второй центарльный момент = {centralMoment(x_values, p_values, 2)}')
    print(
        f'Среднеквдратичное отколнение = квадратный корень от дисперсии = {sko}')
    if ax < 0:
        print(f'Многоугольник или график плотности распределения будут скошены вправо. Ассиметрия = {ax}')
    else:
        print(f'Многоугольник или график плотности распределения будут скошены влево. Ассиметрия = {ax}')
    if ex > 0:
        print(f'Положительный эксцесс обозначает относительно остроконечное распрелеоение. Эксцесс = {ex}')
    else:
        print(f'Отрицательный – относительно сглаженное распределение. Эксцесс = {ex}')

    sum = 0
    for i in range(len(x_values)):
        if x_values[i] <= 0:
            sum += p_values[i]
    print(f' P(X≤x0) = {sum}')

window = Tk()
window.title("Лабораторная работа 1. Вариант 3.")
window.geometry('500x500')
lbl = Label(window, text="Выбери кнопку", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)
btn1 = Button(window, text="Первое задание", command=clicked_btn1)
btn2 = Button(window, text="Второе задание", command=clicked_btn2)
btn3 = Button(window, text="Третее задание", command=clicked_btn3)
# btn4 = Button(window, text="Четвертое задание", command=clicked_btn4)
btn1.grid(column=1, row=0)
btn2.grid(column=1, row=5)
btn3.grid(column=1, row=10)

window.mainloop()
