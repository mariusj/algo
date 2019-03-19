def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

if __name__ == "__main__":
    arr = [5,3,9,2,4,9,1,5]
    insertion_sort(arr)
    print(arr)
