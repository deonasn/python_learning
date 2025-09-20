# Algorithm for Selection Sort

def selection_sort(arr):
    print(f"Selection Sort: {arr}")
    n = len(arr)
    counter = 0
    for i in range(n):
        min_index = i
        swapped = False
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            print(f"{counter}:\t{arr}\t-> Swap Elements: {arr[min_index]} and {arr[i]}")
            arr[i], arr[min_index] = arr[min_index], arr[i]
            counter = counter + 1
            swapped = True
    if not swapped:
        print(f"{counter}:\t{arr}\t-> Elements in Position, Sorted!")
    print("\t=> The list is Sorted!")
    print(f"\tNumber of Swaps made = {counter}")
    return arr


# Simple Algorithm: (no prints)
"""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
"""