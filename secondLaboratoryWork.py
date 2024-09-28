import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from tkinter import *
from scipy.optimize import bisect


# Определяем функцию f(x)
def f(x, k):
    return k * (x + 2)


# Определяем пределы интегрирования
x_min = 0
x_max = 2

# Находим интеграл для определения k
# Интегрируем (x + 2) от 0 до 2
integral_value, _ = quad(lambda x: x + 2, x_min, x_max)

# Условие для плотности вероятности
k = round(1 / integral_value, 3)

print(f"Коэффициент k: {k}")


# Определение функции распределения
def theCmulativeDistributionFunction(x, k):
    gfg = lambda x: f(x, k)
    if x < 0:
        return 0
    elif 0 <= x <= 2:
        integral_value, _ = quad(gfg, 0, x)
        return integral_value
    else:
        return 1


def mathematicalExpectation(a, b):
    mo = (a + b) / 2
    return mo


# Функция для поиска моды
def find_mode(fp, xp):
    fmax = np.max(fp)  # Максимальное значение функции плотности
    ifmax = np.argmax(fp)  # Индекс максимума
    modx = xp[ifmax]  # Мода распределения
    print(f'Мода случайной величины = {modx:.2f}.')  # Вывод результата
    return fmax, ifmax, modx


# Функция для поиска медианы
def find_median(k):
    # Определяем уравнение для решения
    def equation(x):
        return theCmulativeDistributionFunction(x, k) - 0.5
    # Используем метод бисекции для поиска корня уравнения
    median = bisect(equation, 0, 2)  # Ищем корень в интервале [0, 2]
    return median


def clicked_btn1():
    # Создаем массив x для построения графика
    x_values = np.linspace(-1, 3, 800)  # Для отображения от -1 до 3
    y_values = f(x_values, k)

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label=f'f(x) = {k:.2f}(x + 2)', color='blue')
    plt.fill_between(x_values, y_values, where=(x_values >= 0) & (x_values <= 2), alpha=0.3)
    plt.title('График плотности распределения')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.xlim(-1, 3)
    plt.ylim(0, np.max(y_values) + 1)
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.legend()
    plt.grid()
    plt.show()


def clicked_btn2():
    # Создаем массив x для построения графика функции распределения
    x_values = np.linspace(-1, 4, 800)
    F_values = [theCmulativeDistributionFunction(x, k) for x in x_values]

    # Построение графика функции распределения
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, F_values, label='F(x)', color='green')
    plt.title('График функции распределения')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.xlim(-1, 4)
    plt.ylim(-0.1, 1.1)
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.legend()
    plt.grid()
    plt.show()


def clicked_btn3():
    # Вычисление необходимых значений
    mo = mathematicalExpectation(x_min, x_max)
    print(f'Медиана непрерывной случайной величины = {mo}')
    # Генерация значений для функции плотности
    xp = np.linspace(0, 2, 100)  # Значения x от 0 до 2
    fp = [f(x, k) for x in xp]  # Значения функции плотности
    # Поиск моды
    fmax, ifmax, modx = find_mode(fp, xp)
    # Поиск медианы
    median_value = find_median(k)
    print(f'Медиана = {median_value:.2f}.')


window = Tk()
window.title("Лабораторная работа 2. Вариант 3.")
window.geometry('500x500')
lbl = Label(window, text="Выбери кнопку", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)
btn1 = Button(window, text="Первое задание", command=clicked_btn1)
btn1.grid(column=1, row=0)
btn2 = Button(window, text="График функции распределения", command=clicked_btn2)
btn2.grid(column=1, row=1)
btn3 = Button(window, text="Третее задание", command=clicked_btn3)
btn3.grid(column=1, row=2)

window.mainloop()
