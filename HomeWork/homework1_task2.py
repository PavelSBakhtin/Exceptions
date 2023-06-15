# Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий
# новый массив, каждый элемент которого равен разности элементов двух входящих массивов в той же ячейке.
# Если длины массивов не равны, необходимо как-то оповестить пользователя.

def check(arr1, arr2):

    if len(arr1) == len(arr2):
        return True
    return False


def diffArrays(arr1, arr2):
    arr3 = []
    for i, j in zip(arr1, arr2):
        arr3.append(i - j)
    return arr3


if __name__ == '__main__':

    array1 = [1, 2, 3, 4, 5]
    array2 = [2, 3, 4, 5, 6]

    if check(array1, array2):
        print(diffArrays(array1, array2))
    else:
        print("Error! Arrays have different length")
