from random import randint

def find_insert_position(value, a):
    mid = len(a) // 2
    low = 0
    high = len(a) - 1
    if len(a) == 0:
        return 0
    if value > a[-1]:
        return high + 1

    while high - low > 1 and low <= high:
        if value > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        print("Не получилось")
        return -1
    else:
        return mid if a[mid] > value else mid + 1 if value < a[mid + 1] else mid + 2

if __name__ == "__main__":
    a = []
    for i in range(10):
        a.append(randint(1, 50))
    a.sort()
    print(a)

    value = randint(1, 50)
    print(value)

    print(find_insert_position(value, a))