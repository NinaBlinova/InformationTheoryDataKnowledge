import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis

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
