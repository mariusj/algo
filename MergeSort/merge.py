def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        lidx = 0
        ridx = 0
        idx = 0

        while (lidx < len(left) and ridx < len(right)):
            if (left[lidx] <= right[ridx]):
                arr[idx] = left[lidx]
                lidx += 1
            else:
                arr[idx] = right[ridx]
                ridx += 1
            idx += 1

        while lidx < len(left):
            arr[idx] = left[lidx]
            lidx += 1
            idx += 1

        while ridx < len(right):
            arr[idx] = right[ridx]
            ridx += 1
            idx += 1


if __name__ == "__main__":
    arr = [5,3,9,2,4,9,1,5]
    merge_sort(arr)
    print(arr)
