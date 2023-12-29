import random
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Генерация случайных числовых данных
random_data = [random.randint(-10000, 10000) for _ in range(1000)]
series = pd.Series(random_data)

# Вычисление стандартных числовых характеристик
min_value = series.min()
max_value = series.max()
sum_value = series.sum()
mean_value = series.mean()
std_deviation = series.std()

# Вывод результатов в консоль
print("Минимальное значение:", min_value)
print("Количество повторяющихся значений:", len(series[series.duplicated()]))
print("Максимальное значение:", max_value)
print("Сумма значений:", sum_value)
print("Среднеквадратическое отклонение:", std_deviation)

# Визуализация данных: линейный график
plt.plot(series)
plt.title("Линейный график")
plt.xlabel("Индекс")
plt.ylabel("Значение")
plt.show()

# Визуализация данных: гистограмма
rounded_data = series.round(-2) # Округление значений до сотен
plt.hist(rounded_data, bins='auto')
plt.title("Гистограмма")
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.show()

# Создание Dataframe и добавление отсортированных столбцов
df = pd.DataFrame(series, columns=["Значение"])
df["По возрастанию"] = df["Значение"].sort_values()
df["По убыванию"] = df["Значение"].sort_values(ascending=False)

# Визуализация данных: два линейных графика
plt.plot(df["По возрастанию"], label="По возрастанию")
plt.plot(df["По убыванию"], label="По убыванию")
plt.title("Два линейных графика")
plt.xlabel("Индекс")
plt.ylabel("Значение")
plt.legend()
plt.show()