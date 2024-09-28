import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


# Определяем функцию f(x)
def f(x, k):
    return k * (x + 2)


# Определяем пределы интегрирования
x_min = -1
x_max = 1

# Находим интеграл для определения k
# Интегрируем (x + 2) от 0 до 2
integral_value, _ = quad(lambda x: x + 2, x_min, x_max)

# Условие для плотности вероятности
# integral_value * k = 1 => k = 1 / integral_value
k = round(1 / integral_value, 2)

print(f"Коэффициент k: {k}")

# Создаем массив x для построения графика
x_values = np.linspace(-1, 1, 400)  # Для отображения от -1 до 3
y_values = f(x_values, k)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=f'f(x) = {k:.4f}(x + 2)', color='blue')
plt.fill_between(x_values, y_values, where=(x_values >= -1) & (x_values <= 1), alpha=0.3)
plt.title('График плотности распределения')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(-1, 1)
plt.ylim(0, np.max(y_values) + 1)
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.legend()
plt.grid()
plt.show()
