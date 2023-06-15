# Реализуйте 3 метода, чтобы в каждом из них получить разные исключения.
# Посмотрите на код, и подумайте сколько разных типов исключений вы тут сможете получить?

def num2d(string2DArray):
    code = 0
    sum = 0

    if string2DArray == None:
        code = -1
    elif len(string2DArray[0]) < 5:
        code = -2
    else:
        sum = 0
        for i in range(0, len(string2DArray)):
            for j in range(0, 5):
                if string2DArray[i][j].isdigit():
                    val = int(string2DArray[i][j])
                    sum += val
                else:
                    code = -3
                    break
            if code == -3:
                break
    if code == -1:
        print("array is empty")
    elif code == -2:
        print("array wight < 6")
    elif code == -3:
        print("array contains not digit elements")
    else:
        print("summ of  array 6 columns elements are: ")

    return sum


if __name__ == '__main__':

    print(num2d(None))
    array = [["1", "2", "3"], ["4", "5", "6"]]
    print(num2d(array))
    array = [["a", "2", "3", "2", "3", "2", "3"],
             ["4", "5", "6", "2", "3", "2", "3"]]
    print(num2d(array))
    array = [["1", "2", "3", "2", "3", "2", "3"],
             ["4", "5", "6", "2", "3", "2", "3"]]
    print(num2d(array))
