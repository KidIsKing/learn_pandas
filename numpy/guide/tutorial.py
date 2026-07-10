import numpy as np
import time


# ================== СОЗДАНИЕ МАССИВОВ ==================
a = np.array([1, 2, 3])  # Массив
print(a)
print(a.tolist())  # Перевод в лист

a2 = np.array([[1, 2, 3], [4, 5, 6]])  # Двумерный массив
print(a2)  # Будет отображаться, как матрица

# Поддерживаются типы данных float и string
f = np.array([0.1, 0.0045, 0.54])
s = np.array(["Y", "A", "N"])
print(f, s)

# Автозаполнение массивов нулями или единицами, указывая количество элементов
o = np.zeros(5)
e = np.ones(5)
print(o, e)
# Можно передавать кортеж для создания многомерных массивов
shape_a = (3, 2)
a = np.zeros(shape_a)
print(a)
shape_b = (2, 2, 2)  # Форма может быть любая, но отображение будет непонятным
b = np.ones(shape_b)
print(b)

a = np.arange(5)  # От 0 до 4
b = np.arange(1, 10, 5)  # Начало, конец, шаг
print(a, b)

# Создание массива из 5 чисел равнораспределённых между началом и концом включительно
a = np.linspace(0.5, 1, 5)
print(a)

a = np.random.randint(1, 10, 5)  # Создание 5 случайных чисел от 1 до 9
b = np.random.randint(1, 10, (3, 3))  # Матрица заполненная случайными числами
print(a, b)


# ======================== МАТЕМАТИКА ========================
# Вычитание
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = b - a
print(c)

# Аналог без numpy
a = [1, 2, 3]
b = [4, 5, 6]
c = [x - y for x, y in zip(a, b)]
print(c)

# Замерим время с numpy и без
# List
a = list(range(10_000_000))
b = list(range(10_000_000))
start = time.time()
c = [x - y for x, y in zip(a, b)]
print(f"Время вычитания: {time.time() - start} секунд.")  # Медленне

# Array
a = np.arange(10_000_000)
b = np.arange(10_000_000)
start = time.time()
c = a - b
print(f"Время вычитания: {time.time() - start} секунд.")  # Быстрее

# Другие операции для массивов
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# Деление на 0
a = np.array([1])
b = np.array([0])
print(a / b)  # Ошибка не вызовется, но будет сообщение о делении на 0

# В других подобных случаях получится NaN - Not a Number
a = np.array([0])
b = np.array([0])
print(a / b)  # nan

a = np.array([-1]) ** 0.5
print(a)  # nan

print(a[0] is None)  # False, так как Nan != None
print(np.isnan(a))  # Вот так правильно проверить на NaN

# Математика массива и числа аналогична
a = np.array([1, 2, 3])
b = 2
print(a + b)
print(a ** b)

# Выполняются последовательно для каждого элемента и не меняют исходный массив
a = np.array([1, 2, 3])
print(np.exp(a))
print(np.sin(a))

# Произведения из линейной алгебры
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.dot(a, b))  # Число

# Важно соблюдать правило размерностей матриц:
# количество столбцов первой должно совпадать с количеством строк второй
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[2, 4], [1, 3], [5, 7]])
print(a @ b)  # Матричное умножение

# === ПРАКТИКА ===
# Проверить, что sin^2(x) + cos^2(x) = 1, где x - массив чисел
x = np.array([[1, 2, 3], [4, 5, 6]])
x_sin = np.sin(x)
x_cos = np.cos(x)
x_sin_2 = x_sin ** 2
x_cos_2 = x_cos ** 2
print(x_sin_2 + x_cos_2)
print((x_sin_2 + x_cos_2) == 1)  # Не все True из-за точности
print(np.isclose(x_sin_2 + x_cos_2, 1))  # Проверка выражения на близость к 1
# Решение автора урока:
x = np.array([1, 2, 3])
print(np.sin(x) ** 2 + np.cos(x) ** 2)


# ================== СВОЙСТВА МАССИВОВ ==================
a = np.zeros(10)
b = np.zeros((2, 3))
print(a.shape, a.size)  # shape - размерность, всегда кортеж
print(b.shape, b.size)  # size - количество элементов в массиве

# Можно менять размерность с reshape. Создаётся копия, исходник не меняется
a = np.arange(1, 7)
print(a)
print(a.shape)
print(a.reshape(3, 2))
a = a.reshape(3, 2)  # Меняем исходник
print(a)

# Можем указывать -1 и форма исходя из исходника и второго аргумента задастся автоматически
a = a.reshape(-1, 2)
print(a)
a = a.reshape(3, -1)
print(a)

# Меняем многомерный массив на одномерный
a = np.zeros((2, 2))
a = a.reshape(-1)
print(a)

# В массиве могут быть элементы только одного типа данных
a = np.array([1, 2, 3])
b = np.array([1.0, 2.0, 3.0])
print(a.dtype, b.dtype)

# Меняем типы данных
a = a.astype(np.float64)
print(a, a.dtype)
b = b.astype(np.int64)  # Округление вниз
print(b, b.dtype)

a = a.round()  # Округление до ближайшего целого без изменения типа данных
print(a, a.dtype)
a = a.round().astype(np.int64)  # Chaining - объединение вызовов через точку. Применимо, так как каждый метод создаёт копию
print(a, a.dtype)

a = np.array([1, 2, 3])
print(a.min())
print(a.max())
print(a.sum())
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.min())
print(a.max())
print(a.sum())
# Можно передать в аргументы 0 или 1 (строка или столбец, соответственно)
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.min(0))
print(a.max(1))
print(a.sum(1))

a = np.array([True, True, False])
print(a.all())  # Все True
print(a.any())  # Хотя бы 1 True

a = np.array([1, 2, 5])
print(a.mean())  # Среднее
print(a.std())  # Стандартное отклонение

# === ПРАКТИКА ===
# Нормализация: нормализовать массив случайных чисел: привести все элементы к диапазону [0; 1], а потом сделать обратное преобразование
x = np.random.randint(1, 10, (3, 3))
print(x)

x_min = x.min()
x_range = x.max() - x.min()
x = (x - x_min) / x_range
print(x)

x = x * x_range + x_min
print(x)

# Для каждой отдельной колонки
x = np.random.randint(1, 10, (3, 3))
print(x)

x_min = x.min(0)
x_range = x.max(0) - x.min(0)
x = (x - x_min) / x_range
print(x)

x = x * x_range + x_min
print(x)


# ======================== ИНДЕКСАЦИЯ ========================
a = np.array([1, 5, 4, 23, 8])

# Листы умеют
print(a[2])

a[-1] = 5
print(a)

print(a[1:3])
print(a[3:])
print(a[:2])
print(a[:])
print(a[1:3:-1])  # Начало : конец : шаг
print(a[::-1])

a[1:3] = np.array([1, 2])  # Перезаписываем целый диапазон, главное совпасть с размерностью среза
print(a, a[1:3])

# Листы не умеют
print(a[[1, 4]])  # Список из элементов на указанных индексах

a = np.array([[1, 5], [67, 52]])
print(a[0])  # Строка под индексом 0
print(a[1][0])  # Конкретный элемент
print(a[1, 0])  # Конкретный элемент. Другая форма записи. Двумерные листы не поддерживают такую запись
print(a[:, 1])  # Столбец под индексом 1

# Булевская индексация
a = np.array([1, 2, 3, 4])
index = [True, False, False, True]
print(a[index])  # Берём элементы, где в index True

# Более реальное применение. Например, находим четные
b = a % 2 == 0
print(b)  # Список булевых значений
b = a[a % 2 == 0]
print(b)  # Список значений, где True

# Комбинированные условия: and - &, or - |, not - ~
b = a[(a % 2 == 0) & ~(a % 3 == 0)]  # == (b = a[(a % 2 == 0) & (a % 3 != 0)])
print(b)

# === ПРАКТИКА ===
# Фильтр выбросов: убрать выбросы из массива: удалить все элементы, которые больше среднего в 3 раза или меньше 1/3 от среднего
x = np.array([1, 20, 30, 100, 40, 5, 200])
midd = x.mean()
f = x[(x <= midd*3) & (x >= midd/3)]
print(x, midd, f)


# NumPy используется в Pandas, Scipy, Scikit-Learn. На смену NumPy с тензорами пришли PyTorch, Jax, TensorFlow
