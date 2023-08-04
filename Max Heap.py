class Heap:
    @staticmethod
    def heapify(arr: [float], i: int) -> None:
        n = len(arr)
        largest = i
        left = 2 * i + 1 if 2 * i + 1 < n else None
        right = 2 * i + 2 if 2 * i + 2 < n else None

        if left is not None and arr[i] < arr[left]:
            largest = left

        if right is not None and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            Heap.heapify(arr, largest)

    @staticmethod
    def insert(arr: [float], val: float) -> None:
        if len(arr) == 0:
            arr.append(val)
            return
        arr.append(val)
        for i in range((len(arr) // 2) - 1, -1, -1):
            Heap.heapify(arr, i)

    @staticmethod
    def delete(arr: [float], val: float) -> None:
        ind = arr.index(val)
        arr[ind], arr[len(arr) - 1] = arr[len(arr) - 1], arr[ind]
        del arr[len(arr) - 1]
        for i in range((len(arr) // 2) - 1, -1, -1):
            Heap.heapify(arr, i)


if __name__ == '__main__':
    temp = [9, 3, 7, 1, 4, 2, 5]
    print(f"Initial dataset = {temp}")
    array = []
    for i in temp:
        Heap.insert(array, i)
    print(f"Heap based on dataset = {array}")
    Heap.delete(array, 7)
    print(f"Heap after deleting 7 = {array}")
    Heap.delete(array, 3)
    print(f"Heap after deleting 3 = {array}")
