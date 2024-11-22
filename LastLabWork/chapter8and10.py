import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis
from scipy import stats


# Загрузка данных из файла
data = pd.read_csv('var3.txt', delimiter=' ', header=None)

# Преобразование строк в числовой формат
data = data.apply(lambda x: x.str.replace(',', '.').astype(float) if x.dtype == "object" else x)

x = data.values.flatten()  # Преобразование в одномерный массив

# Вычисления
n = len(x)  # Объем выборки
xmin = np.min(x)  # Минимальное значение
xmax = np.max(x)  # Максимальное значение
Mx = np.mean(x)  # Выборочное математическое ожидание
f = n - 1  # Число степеней свободы
Dx = np.var(x, ddof=1)  # Выборочная дисперсия
Sx = np.std(x, ddof=1)  # Среднеквадратичное отклонение
Ax = skew(x)  # Асимметрия
Ex = kurtosis(x) - 3  # Эксцесс
Medx = np.median(x)  # Медиана
Rx = np.ptp(x)  # Размах выборки

# Вывод результатов
print(f'Объем выборки n={n}')
print(f'xmin={xmin:.7f}')
print(f'xmax={xmax:.7f}')
print(f'Выборочное математическое ожидание Mx={Mx:.7f}')
print(f'Число степеней свободы выборки f={f}')
print(f'Выборочная дисперсия Dx={Dx:.7f}')
print(f'Среднеквадратичное отклонение Sx={Sx:.7f}')
print(f'Асимметрия Ax={Ax:.7f}')
print(f'Эксцесс Ex={Ex:.7f}')
print(f'Медиана Medx={Medx:.7f}')
print(f'Размах Rx={Rx:.7f}')



# Загрузка данных из файла
data = pd.read_csv('var3.txt', delimiter=' ', header=None)

# Преобразование строк в числовой формат
data = data.apply(lambda x: x.str.replace(',', '.').astype(float) if x.dtype == "object" else x)

# Проверяем содержимое DataFrame
print("Содержимое DataFrame:")
print(data)

# Проверяем наличие NaN и удаляем их (если необходимо)
data = data.dropna()

x = data.values  # Преобразование в массив numpy

# Доверительные вероятности
p = np.array([0.9, 0.95, 0.99, 0.999])
q = 1 - p

# Доверительные интервалы для генерального математического ожидания
Mx = np.mean(x, axis=0)
n = x.shape[0]
Mxd = []

for q_val in q:
    ci = stats.t.interval(q_val, n-1, loc=Mx, scale=stats.sem(x, axis=0))
    Mxd.append((q_val, ci[0], ci[1]))

print('Доверительные интервалы для генерального МО:')
for q_val, lower_bound, upper_bound in Mxd:
    print(f'p={1 - q_val:.4f}:', end=' ')
    for lb, ub in zip(lower_bound, upper_bound):
        print(f'{lb:.6f} <= mx <= {ub:.6f}', end=' ')
    print()  # Переход на новую строку после каждого p_val

# Доверительные интервалы для генеральной дисперсии
Dx = np.var(x, axis=0, ddof=1)
chi2l = stats.chi2.ppf(1 - q / 2, n - 1)
chi2r = stats.chi2.ppf(q / 2, n - 1)

Dxd = []
for i in range(len(p)):
    lower_bound = (n - 1) * Dx[i] / chi2l[i]
    upper_bound = (n - 1) * Dx[i] / chi2r[i]
    Dxd.append((p[i], lower_bound, upper_bound))

print('Доверительные интервалы для генеральной дисперсии:')
for p_val, lower, upper in Dxd:
    print(f'p={p_val:.4f}:   {lower:.6f} <= Dx <= {upper:.6f}')

# Дисперсия Ax и Ex
Da = 6 * (n - 1) / (n + 1) / (n + 3)
De = 24 * n * (n - 2) * (n - 3) / (n + 1)**2 / (n + 3) / (n + 5)

print(f'Da={Da:.5f}\nDe={De:.5f}')

# Доверительные интервалы для генеральной асимметрии
Ax = stats.skew(x, axis=0)
Axd = []
for q_val in q:
    lower_bound = Ax - (Da / q_val)**0.5
    upper_bound = Ax + (Da / q_val)**0.5
    Axd.append((q_val, lower_bound, upper_bound))

print('Доверительные интервалы для генеральной асимметрии:')
for q_val, lower, upper in Axd:
    print(f'p={1 - q_val:.4f}:', end=' ')
    for lb, ub in zip(lower, upper):
        print(f'{lb:.6f} <= ax <= {ub:.6f}', end=' ')
    print()

# Доверительные интервалы для генерального эксцесса
Ex = stats.kurtosis(x, axis=0)
Exd = []
for q_val in q:
    lower_bound = Ex - (De / q_val)**0.5
    upper_bound = Ex + (De / q_val)**0.5
    Exd.append((q_val, lower_bound, upper_bound))

print('Доверительные интервалы для генерального эксцесса:')
for q_val, lower, upper in Exd:
    print(f'p={1 - q_val:.4f}:', end=' ')
    for lb, ub in zip(lower, upper):
        print(f'{lb:.6f} <= ex <= {ub:.6f}', end=' ')
    print()