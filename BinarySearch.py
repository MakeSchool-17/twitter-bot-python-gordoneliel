''' Binary Search '''


def binarySearch(list, data):

    mid = len(list) // 2
    if len(list) <= 0:
        return False
    if list[mid] == data:
        return list[mid]
    else:
        if list[mid] > data:
            return binarySearch(list[: mid - 1], data)
        elif list[mid] < data:
            return binarySearch(list[mid + 1:], data)


def main():
    list = []
    for i in range(100):
        list.append(i)
    gotValue = binarySearch(list, 5)
    print(gotValue)
    print(list)


if __name__ == "__main__":
    main()
