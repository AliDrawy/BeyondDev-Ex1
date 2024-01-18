
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already sorted, no need to check them
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the two sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less_than_pivot = []

    for x in arr[1:]:
        if x <= pivot:
            less_than_pivot.append(x)

    greater_than_pivot = []

    for x in arr[1:]:
        if x > pivot:
            greater_than_pivot.append(x)

    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

if __name__ == '__main__':
    # Q5-1
    arr_bubble = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr_bubble)
    print("Bubble Sorted Array:", arr_bubble)
    # Q5-2
    arr_merge = [64, 34, 25, 12, 22, 11, 90]
    merge_sort(arr_merge)
    print("Merge Sorted Array:", arr_merge)
    # Q5-3
    arr_quick = [64, 34, 25, 12, 22, 11, 90]
    arr_quick = quicksort(arr_quick)
    print("Quicksort Sorted Array:", arr_quick)

    # Q10-1

    # 1-Bubble Sort:
    # Worst-case time complexity: O(n^2) - Occurs when the input array is in reverse order, and each element needs to be swapped in every pass.
    # Best-case time complexity: O(n) - Occurs when the input array is already sorted, and no swaps are needed.
    # Average-case time complexity: O(n^2) - On average, Bubble Sort performs poorly compared to more advanced algorithms.

    # 2-Merge Sort:
    # Worst-case time complexity: O(n log n) - Regardless of the input, Merge Sort consistently has a time complexity of O(n log n) due to its divide-and-conquer nature.
    # Best-case time complexity: O(n log n) - Similar to the worst case, as Merge Sort always divides the array into halves until it reaches single elements.
    # Average-case time complexity: O(n log n) - Merge Sort is efficient on average and widely used for its stable and predictable performance.

    # 3-Quicksort:
    # Worst-case time complexity: O(n^2) - Occurs when the pivot selection consistently results in unbalanced partitions. This can be mitigated with randomized or carefully chosen pivot strategies.
    # Best-case time complexity: O(n log n) - Occurs when the pivot selection consistently results in balanced partitions.
    # Average-case time complexity: O(n log n) - Quicksort has good average-case performance and is often faster in practice compared to other O(n log n) algorithms.#