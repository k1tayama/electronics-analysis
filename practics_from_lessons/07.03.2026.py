import numpy as np 

a = np.array([1, 2, 3, 4, 5, 6])
# print(a)

b = np.arange(10, 15) # генерация массива 
# print(b)

num = np.random.randint(5)
# print(num)

arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)
# print(arr[1][2])

# print(arr.ndim) #размерность
# print(arr.shape) #кол-во элементов
# print(arr.mean())

# print(a)
# print(a[a>3])
# print(np.sum(a>3))
# print(a.prod()) # произведение элементов
# print(a**2)
# print(a.reshape(2, 3)) #изменение размерности массива 



# ----------------------------------------------------------------------------------------------------------

import numpy as np
class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 2
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < self.current: raise StopIteration("вышли за предел")
        else: 
            value = self.current
            self.current += 2
            return value
# for x in EvenIterator(10):
#     print(x)

class ReverseList:
    def __init__(self, spisok):
        self.spisok = spisok
        self.current = len(spisok)-1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < 0: raise StopIteration("индекс ушел за начало списка")
        else:
            value = self.spisok[self.current]
            self.current -= 1
            return value
# data = [10, 20, 30]
# for x in ReverseList(data):
#     print(x) 

# 3 
arr = np.array([3, 7, 1, 9, 4])
# print(f"Максимальный элемент: {arr.max()}")
# print(f"Cреднее значение массива: {arr.mean()}")

# 4
# arr = np.array([2, 8, 4, 10, 3])
# print(arr[arr>5])

# 5
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(a+b)

#6
arr = np.array([1, 2, 3, 4])
arr_new = arr*3
print(arr_new)