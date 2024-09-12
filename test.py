import numpy as np
import matplotlib.pyplot as plt

# Заданные значения
x_values = np.array([-2, -1, 0, 1, 2, 3, 4])
p_values = np.array([0.05, 0.1, 0.18, 0.25, 0.2, 0.12])

# Проверка, чтобы сумма вероятностей равнялась 1
if np.sum(p_values) != 1:
    p_values = np.append(p_values, 1 - np.sum(p_values))  # Добавляем недостающее значение

# Вычисляем функцию распределения
F = np.cumsum(p_values)

# Подготавливаем данные для графика
x1 = np.concatenate(([x_values[0] - 0.5], x_values, [x_values[-1] + 0.5]))
F1 = np.concatenate(([0], F, [1]))

# Вычисляем промежутки
intervals = [f"{x_values[i]}-{x_values[i+1]}" for i in range(len(x_values) - 1)]

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
data = {'Интервал': intervals, 'P(X)': p_values[:-1]}  # Убираем последнее значение вероятности
table_data = np.array(list(zip(intervals, p_values[:-1])))

# Добавляем таблицу рядом с графиком
plt.table(cellText=table_data,
          colLabels=['Интервал', 'P(X)'],
          cellLoc='center',
          loc='right',
          bbox=[1.05, 0.1, 0.4, 0.8])

# Показываем график
plt.legend()
plt.tight_layout()
plt.show()
