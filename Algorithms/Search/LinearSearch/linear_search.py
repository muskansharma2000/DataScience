def linear_search(a, e):
    for i in range(0, len(a)):
        if a[i] == e:
            return i


# Example:
array = [7, 3, 8, 1, 6, 9, 2]
position = linear_search(array, 1)
print(position)
