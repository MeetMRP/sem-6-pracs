import random
import time
import copy


def Lomuto_partition(low: int, high: int, data: list) -> int:
    i = low
    j = low
    pivot = data[high]

    while j < high:
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
        j += 1

    data[i], data[high] = data[high], data[i]
    return i


def hoare_partition(low: int, high: int, data: list) -> int:
    pivot = data[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while data[i] < pivot:
            i += 1
        j -= 1
        while data[j] > pivot:
            j -= 1
        if i >= j:
            return j
        data[i], data[j] = data[j], data[i]

# hoare


def quick_sort_hoare(low: int, high: int, data: list) -> None:
    if low < high:
        p = hoare_partition(low, high, data)
        quick_sort_hoare(low, p, data)
        quick_sort_hoare(p + 1, high, data)


def randomized_partition_hoare(low: int, high: int, data: list):
    random_index = random.randint(low, high)
    data[random_index], data[low] = data[low], data[random_index]
    return hoare_partition(low, high, data)


def quick_sort_hoare_with_rand(low: int, high: int, data: list) -> list:
    if low < high:
        p = randomized_partition_hoare(low, high, data)
        quick_sort_hoare(low, p-1, data)
        quick_sort_hoare(p+1, high, data)

# lomuto


def quick_sort(low: int, high: int, data: list) -> list:
    if low < high:
        p = Lomuto_partition(low, high, data)
        quick_sort(low, p-1, data)
        quick_sort(p+1, high, data)


def randomized_partition_lomuto(low: int, high: int, data: list) -> int:
    random_index = random.randint(low, high)
    data[random_index], data[high] = data[high], data[random_index]
    return Lomuto_partition(low, high, data)


def quick_sort_with_rand(low: int, high: int, data: list) -> list:
    if low < high:
        p = randomized_partition_lomuto(low, high, data)
        quick_sort(low, p-1, data)
        quick_sort(p+1, high, data)


def get_data(n) -> list:
    return [random.randint(1, 100000) for _ in range(n)]


n = 10000
data1: list = get_data(n)
data2: list = copy.deepcopy(data1)
data3: list = copy.deepcopy(data1)
data4: list = copy.deepcopy(data1)
# data = [2, 45, 72, 92, 1, 31, 0, 42]
low = 0
high = n-1

start = time.time()
quick_sort(low, high, data1)
end = time.time()
print("time for lomuto: ", end-start)

start = time.time()
quick_sort_with_rand(low, high, data2)
end = time.time()
print("time for lomuto with randomized pivot: ", end-start)

start = time.time()
quick_sort_hoare(low, high, data3)
end = time.time()
print("time for hoards: ", end-start)

start = time.time()
quick_sort_hoare_with_rand(low, high, data4)
end = time.time()
print("time for hoards with randomized pivot: ", end-start)
