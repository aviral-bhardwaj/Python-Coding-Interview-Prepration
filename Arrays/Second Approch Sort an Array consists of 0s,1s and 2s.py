def swap(array, low, high):
    temp = array[low]
    array[low] = array[high]
    array[high] = temp


def sorting_array(array, end):
    start = mid = 0
    pivot = 1

    while mid <= end:
        if array[mid] < pivot:
            swap(array, start, mid)
            start = start + 1
            mid = mid + 1
        elif array[mid] > pivot:
            swap(array, mid, end)
            end = end - 1
        else:
            mid = mid + 1


if __name__ == '__main__':
    array = [2, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    sorting_array(array, len(array) - 1)
    print(array)
