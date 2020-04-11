def binary_search_recursive(a, left, right, e):
    if left <= right:
        middle = left + int((right - left) / 2)
        if a[middle] == e:
            return middle
        elif a[middle] < e:
            return binary_search_recursive(a, middle + 1, right, e)
        else:
            return binary_search_recursive(a, left, middle - 1, e)


def binary_search(a, left, right, e):
    while left <= right:
        middle = left + int((right - left) / 2)
        if a[middle] == e:
            return middle
        elif a[middle] < e:
            left = middle + 1
        else:
            right = middle - 1


# Example:
array = [1, 2, 3, 4, 5, 6, 7, 8]
position = binary_search_recursive(array, 0, 7, 2)
print(position)