import random
import time
import matplotlib.pyplot as plt

# ------------------------------
# Детермінований QuickSort
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

# ------------------------------
# Рандомізований QuickSort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# ------------------------------
# Вимірювання часу
def measure_time(sort_func, arr, repeat=5):
    times = []
    for _ in range(repeat):
        arr_copy = arr.copy()
        start = time.perf_counter()
        sort_func(arr_copy)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / repeat

# ------------------------------
# Тестування
sizes = [10_000, 50_000, 100_000, 500_000]
randomized_times = []
deterministic_times = []

for size in sizes:
    arr = [random.randint(0, size) for _ in range(size)]
    print(f"Розмір масиву: {size}")

    rand_time = measure_time(randomized_quick_sort, arr)
    print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")
    randomized_times.append(rand_time)

    det_time = measure_time(deterministic_quick_sort, arr)
    print(f"   Детермінований QuickSort: {det_time:.4f} секунд")
    deterministic_times.append(det_time)

# ------------------------------
# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(sizes, randomized_times, marker='o', label='Рандомізований QuickSort')
plt.plot(sizes, deterministic_times, marker='s', label='Детермінований QuickSort')
plt.title("Порівняння ефективності QuickSort")
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.legend()
plt.grid(True)
plt.tight_layout()
# plt.show()
plt.savefig("graf.png")