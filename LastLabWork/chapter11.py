from tkinter import Tk, Label, Button

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Загрузка данных из файла
data = pd.read_csv('var3.txt', delimiter=' ', header=None)

# Преобразование строк в числовой формат
data = data.apply(lambda x: x.str.replace(',', '.').astype(float) if x.dtype == "object" else x)

# Проверка содержимого DataFrame
print("Содержимое DataFrame:")
print(data)

# Выбор одного из столбцов для анализа (например, первого)
x = data.iloc[:, 0].dropna().values  # Убедитесь, что выбрали нужный столбец

# Простейший тест на нормальность (критерий Шапиро-Уилка)
alpha = 0.05
shapiro_test = stats.shapiro(x)
print(f'\nПростейший тест: W={shapiro_test.statistic:.4f}, p-value={shapiro_test.pvalue:.4f}')
if shapiro_test.pvalue < alpha:
    print('Отвергаем основную гипотезу о нормальности.')
else:
    print('Принимаем основную гипотезу о нормальности.')

# Тест Жарка-Бера
jb_test = stats.jarque_bera(x)
print(f'\nТест Жарка-Бера: JB={jb_test.statistic:.4f}, p-value={jb_test.pvalue:.4f}')
if jb_test.pvalue < alpha:
    print('Отвергаем основную гипотезу о нормальности.')
else:
    print('Принимаем основную гипотезу о нормальности.')

# Построение гистограммы распределения
plt.figure(figsize=(10, 6))
k = round(len(x)**0.5)  # число интервалов
h = (np.max(x) - np.min(x)) / k  # ширина интервала

# Вывод числа интервалов и ширины интервала в консоль
print(f'\nЧисло интервалов k: {k}')
print(f'Ширина интервала h: {h:.4f}')
plt.hist(x, bins=k, alpha=0.7, color='blue', edgecolor='black')
plt.title('Гистограмма')
plt.xlabel('x')
plt.ylabel('Частота')
plt.grid()
plt.show()

# Подбор параметров для различных теоретических распределений
distributions = {
    'gumbel_r': 'Гамбеловское (правостороннее)',
    'expon': 'Экспоненциальное',
    'gamma': 'Гамма',
    'lognorm': 'Логнормальное',
    'norm': 'Нормальное',
    'rayleigh': 'Рэлеевское',
    'uniform': 'Равномерное',
    'weibull_min': 'Вейбулловское'
}

params = {}
for dist_name in distributions.keys():
    # Подбор параметров для каждого распределения
    if dist_name == 'norm':
        param = stats.norm.fit(x)
    elif dist_name == 'gumbel_r':
        param = stats.gumbel_r.fit(x)
    elif dist_name == 'expon':
        param = stats.expon.fit(x)
    elif dist_name == 'gamma':
        param = stats.gamma.fit(x)
    elif dist_name == 'lognorm':
        param = stats.lognorm.fit(x)
    elif dist_name == 'rayleigh':
        param = stats.rayleigh.fit(x)
    elif dist_name == 'uniform':
        param = stats.uniform.fit(x)
    elif dist_name == 'weibull_min':
        param = stats.weibull_min.fit(x)

    params[dist_name] = param

print('\nПараметры различных распределений по МПП:')
for dist_name, param in params.items():
    if dist_name == 'norm':
        print(f'{distributions[dist_name]}: mu={param[0]:.4f}, sigma={param[1]:.4f}')
    elif dist_name == 'gumbel_r':
        print(f'{distributions[dist_name]}: loc={param[0]:.4f}, scale={param[1]:.4f}')
    elif dist_name == 'gamma':
        print(f'{distributions[dist_name]}: a={param[0]:.4f}, loc={param[1]:.4f}, scale={param[2]:.4f}')
    elif dist_name == 'lognorm':
        print(f'{distributions[dist_name]}: shape={param[0]:.4f}, loc={param[1]:.4f}, scale={param[2]:.4f}')
    elif dist_name == 'rayleigh':
        print(f'{distributions[dist_name]}: scale={param[0]:.4f}')
    elif dist_name == 'expon':
        print(f'{distributions[dist_name]}: loc={param[0]:.4f}, scale={param[1]:.4f}')
    elif dist_name == 'uniform':
        print(f'{distributions[dist_name]}: loc={param[0]:.4f}, scale={param[1]:.4f}')
    elif dist_name == 'weibull_min':
        print(f'{distributions[dist_name]}: c={param[0]:.4f}, loc={param[1]:.4f}, scale={param[2]:.4f}')

# Выбор одного из столбцов для анализа (например, первого)
x = data.iloc[:, 0].dropna().values  # Убедитесь, что выбрали нужный столбец

# Эмпирическая функция распределения
ecdf_x = np.sort(x)
ecdf_y = np.arange(1, len(ecdf_x) + 1) / len(ecdf_x)

# График эмпирической функции распределения и теоретических распределений
plt.figure(figsize=(10, 6))
plt.step(ecdf_x, ecdf_y, label='Эмпирическая функция', where='post')

# Список распределений для подгонки
distributions = ['norm', 'expon', 'gamma', 'lognorm', 'weibull_min']
params = {}

# Подбор параметров и графиков теоретических распределений
x_range = np.linspace(min(ecdf_x), max(ecdf_x), 1000)

for dist_name in distributions:
    # Подбор параметров для каждого распределения
    param = getattr(stats, dist_name).fit(x)
    params[dist_name] = param

    # Получение теоретической функции плотности вероятности (PDF)
    if dist_name == 'norm':
        pdf = stats.norm.pdf(x_range, *param)
    elif dist_name == 'expon':
        pdf = stats.expon.pdf(x_range, *param)
    elif dist_name == 'gamma':
        pdf = stats.gamma.pdf(x_range, *param)
    elif dist_name == 'lognorm':
        pdf = stats.lognorm.pdf(x_range, *param)
    elif dist_name == 'weibull_min':
        pdf = stats.weibull_min.pdf(x_range, *param)

    plt.plot(x_range, pdf, label=f'{dist_name} распределение')

plt.title('Эмпирическая и теоретические функции распределения')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()

# Проверка наилучшего распределения по критерию Колмогорова
best_dist = None
best_p_value = 0

for dist_name in distributions:
    param = params[dist_name]

    # Получение теоретической функции распределения (CDF)
    if dist_name == 'norm':
        cdf = stats.norm.cdf(ecdf_x, *param)
    elif dist_name == 'expon':
        cdf = stats.expon.cdf(ecdf_x, *param)
    elif dist_name == 'gamma':
        cdf = stats.gamma.cdf(ecdf_x, *param)
    elif dist_name == 'lognorm':
        cdf = stats.lognorm.cdf(ecdf_x, *param)
    elif dist_name == 'weibull_min':
        cdf = stats.weibull_min.cdf(ecdf_x, *param)

    # Критерий Колмогорова
    d_statistic, p_value = stats.ks_2samp(ecdf_y, cdf)

    if p_value > best_p_value:
        best_p_value = p_value
        best_dist = dist_name

print(
    f'\nКритерий согласия Колмогорова:\nЛучше всего подходит {best_dist} распределение;\nКритический уровень значимости для него = {best_p_value:.5f}')

# График эмпирической функции распределения и подобранной теоретической функции распределения
plt.figure(figsize=(10, 6))
plt.step(ecdf_x, ecdf_y, label='Эмпирическая функция', where='post')

# Подбор параметров для наилучшего распределения
best_param = params[best_dist]
x_range_cdf = np.linspace(min(ecdf_x), max(ecdf_x), 1000)

if best_dist == 'norm':
    best_cdf = stats.norm.cdf(x_range_cdf, *best_param)
elif best_dist == 'expon':
    best_cdf = stats.expon.cdf(x_range_cdf, *best_param)
elif best_dist == 'gamma':
    best_cdf = stats.gamma.cdf(x_range_cdf, *best_param)
elif best_dist == 'lognorm':
    best_cdf = stats.lognorm.cdf(x_range_cdf, *best_param)
elif best_dist == 'weibull_min':
    best_cdf = stats.weibull_min.cdf(x_range_cdf, *best_param)

plt.plot(x_range_cdf, best_cdf, color='green', label=f'Подобранное {best_dist} распределение')
plt.title(f'Подобрано {best_dist} распределение')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.legend()
plt.grid()
plt.show()