# provide a bubble sort that shorts integers
def bubble_sort(arr):
    """Sort a list of integers in ascending order using the bubble sort algorithm."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# write test function
def test_bubble_sort():
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    assert arr == [11, 12, 22, 25, 34, 64, 90], f"Expected [11, 12, 22, 25, 34, 64, 90] but got {arr}"

test_bubble_sort()

