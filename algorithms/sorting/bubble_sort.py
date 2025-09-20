# Algorithm for Bubble Sort

def bubble_sort(arr):
    print(f"Bubble Sort: {arr}")
    n = len(arr)
    counter = 0
    for i in range(n -1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                print(f"{counter}:\t{arr}\t-> Swap Elements: {arr[j]} and {arr[j + 1]}")
                counter += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            print(f"{counter}:\t{arr}\t-> Elements in Position, Sorted!")
            break
    print("\t=> The list is Sorted!")
    print(f"\tNumber of Swaps made = {counter - 1}")
    return arr


# Simple Algorithm: (no prints)
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n -1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
"""