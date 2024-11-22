import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных из Excel без заголовков
file_path = 'data.xlsx'
df = pd.read_excel(file_path, header=None)

# Задание названий столбцов
df.columns = ['Территория', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

# Извлечение месяцев (1-12)
months = np.arange(1, 13)  # Предполагаем, что у нас 12 месяцев

# Функция для извлечения зарплаты и проверки длины
def get_salary(territory_name):
    salary = df.loc[df['Территория'] == territory_name, df.columns[1:]].values.flatten()
    return salary if salary.size > 0 else None

Karelia_salary = get_salary('Карелия')
Kaliningrad_salary = get_salary('Калининград')
Novgorod_salary = get_salary('Новгород')
Spb_salary = get_salary('Спб')


# Проверка длины массивов перед полиномиальной аппроксимацией
def fit_polynomial(months, salary):
    if salary is not None and len(salary) == len(months):
        return np.polyfit(months, salary, 2)
    return None

# Получение коэффициентов полиномов
coeffs_Karelia = fit_polynomial(months, Karelia_salary)
coeffs_Kaliningrad = fit_polynomial(months, Kaliningrad_salary)
coeffs_Novgorod = fit_polynomial(months, Novgorod_salary)
coeffs_Spb = fit_polynomial(months, Spb_salary)

# Создание полиномов
poly_Karelia = np.poly1d(coeffs_Karelia) if coeffs_Karelia is not None else None
poly_Kaliningrad = np.poly1d(coeffs_Kaliningrad) if coeffs_Kaliningrad is not None else None
poly_Novgorod = np.poly1d(coeffs_Novgorod) if coeffs_Novgorod is not None else None
poly_Spb = np.poly1d(coeffs_Spb) if coeffs_Spb is not None else None

# Генерация точек для графика
x_fit = np.linspace(1, 12, 100)
y_fit_Karelia = poly_Karelia(x_fit) if poly_Karelia is not None else None
y_fit_Kaliningrad = poly_Kaliningrad(x_fit) if poly_Kaliningrad is not None else None
y_fit_Novgorod = poly_Novgorod(x_fit) if poly_Novgorod is not None else None
y_fit_Spb= poly_Spb(x_fit) if poly_Spb is not None else None

# Визуализация
plt.figure(figsize=(12, 12))

# График для Карелии
plt.subplot(4, 1, 1)
if Karelia_salary is not None:
    plt.scatter(months[:len(Karelia_salary)], Karelia_salary, color='red', label='Исходные данные (Карелия)')
    plt.plot(x_fit, y_fit_Karelia, color='blue', label='Аппроксимация (Карелия)')
plt.title('Зарплата в Карелии')
plt.xlabel('Месяц')
plt.ylabel('Зарплата (руб.)')
plt.legend()
plt.grid()

# График для Калининграда
plt.subplot(4, 1, 2)
if Kaliningrad_salary is not None:
    plt.scatter(months[:len(Kaliningrad_salary)], Kaliningrad_salary, color='green', label='Исходные данные (Калининград)')
    plt.plot(x_fit, y_fit_Kaliningrad, color='blue', label='Аппроксимация (Калининград)')
plt.title('Зарплата в Калининграде')
plt.xlabel('Месяц')
plt.ylabel('Зарплата (руб.)')
plt.legend()
plt.grid()

# График для Новгорода
plt.subplot(4, 1, 3)
if Novgorod_salary is not None:
    plt.scatter(months[:len(Novgorod_salary)], Novgorod_salary, color='orange', label='Исходные данные (Новгород)')
    plt.plot(x_fit, y_fit_Novgorod, color='blue', label='Аппроксимация (Новгород)')
plt.title('Зарплата в Новгороде')
plt.xlabel('Месяц')
plt.ylabel('Зарплата (руб.)')
plt.legend()
plt.grid()

# График для Спб
plt.subplot(4, 1, 4)
if Spb_salary is not None:
    plt.scatter(months[:len(Spb_salary)], Spb_salary, color='black', label='Исходные данные (Спб)')
    plt.plot(x_fit, y_fit_Spb, color='blue', label='Аппроксимация (Спб)')
plt.title('Зарплата в Спб')
plt.xlabel('Месяц')
plt.ylabel('Зарплата (руб.)')
plt.legend()
plt.grid()


plt.tight_layout()
plt.show()

# Вывод коэффициентов полиномов

print("\nБазисные функции и коэффициенты полиномов:")
products = ['Карелия', 'Калининград', 'Новгород', 'Спб']
coeffs_list = [coeffs_Karelia, coeffs_Kaliningrad, coeffs_Novgorod, coeffs_Spb]

for product, coeffs in zip(products, coeffs_list):
    if coeffs is not None:
        print(f"{product}: Базисные функции: (x^2, x^1, 1) -> Коэффициенты: {coeffs}")
    else:
        print(f"{product}: Нет данных для аппроксимации.")
