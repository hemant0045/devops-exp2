class SortingAlgorithms:

    # 1. Bubble Sort
    def bubble_sort(self, arr):
        n = len(arr)

        for i in range(n - 1):
            swapped = False

            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            if not swapped:
                break

        return arr

    # 2. Selection Sort
    def selection_sort(self, arr):
        n = len(arr)

        for i in range(n - 1):
            min_index = i

            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr

    # 3. Insertion Sort
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1

            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key

        return arr

    # 4. Merge Sort
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    # 5. Quick Sort
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[-1]

        left = []
        middle = []
        right = []

        for x in arr:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)

        return self.quick_sort(left) + middle + self.quick_sort(right)

    # 6. Heap Sort
    def heap_sort(self, arr):
        n = len(arr)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Extract elements
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)

        return arr

    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    # 7. Shell Sort
    def shell_sort(self, arr):
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i

                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap

                arr[j] = temp

            gap //= 2

        return arr

    # 8. Counting Sort
    def counting_sort(self, arr):
        if not arr:
            return arr

        # Counting sort for non-negative integers
        if min(arr) < 0:
            print("Counting Sort supports non-negative integers only.")
            return arr

        maximum = max(arr)

        count = [0] * (maximum + 1)

        for num in arr:
            count[num] += 1

        result = []

        for i in range(len(count)):
            result.extend([i] * count[i])

        return result

    # 9. Radix Sort
    def radix_sort(self, arr):
        if not arr:
            return arr

        # Radix sort for non-negative integers
        if min(arr) < 0:
            print("Radix Sort supports non-negative integers only.")
            return arr

        maximum = max(arr)
        place = 1

        while maximum // place > 0:
            arr = self.counting_sort_by_digit(arr, place)
            place *= 10

        return arr

    def counting_sort_by_digit(self, arr, place):
        output = [0] * len(arr)
        count = [0] * 10

        for num in arr:
            digit = (num // place) % 10
            count[digit] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(len(arr) - 1, -1, -1):
            digit = (arr[i] // place) % 10
            output[count[digit] - 1] = arr[i]
            count[digit] -= 1

        return output

    # 10. Bucket Sort
    def bucket_sort(self, arr):
        if len(arr) == 0:
            return arr

        min_value = min(arr)
        max_value = max(arr)

        bucket_count = len(arr)
        buckets = [[] for _ in range(bucket_count)]

        # Put elements into buckets
        for num in arr:
            if max_value == min_value:
                index = 0
            else:
                index = int(
                    (num - min_value) *
                    (bucket_count - 1) /
                    (max_value - min_value)
                )

            buckets[index].append(num)

        # Sort individual buckets using insertion sort
        result = []

        for bucket in buckets:
            self.insertion_sort(bucket)
            result.extend(bucket)

        return result


# Main class
class Main:

    def run(self):
        sorting = SortingAlgorithms()

        print("----- SORTING ALGORITHMS -----")

        arr = list(map(int, input("Enter elements: ").split()))

        print("\nOriginal Array:")
        print(arr)

        print("\nChoose Sorting Algorithm:")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Heap Sort")
        print("7. Shell Sort")
        print("8. Counting Sort")
        print("9. Radix Sort")
        print("10. Bucket Sort")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            result = sorting.bubble_sort(arr.copy())

        elif choice == 2:
            result = sorting.selection_sort(arr.copy())

        elif choice == 3:
            result = sorting.insertion_sort(arr.copy())

        elif choice == 4:
            result = sorting.merge_sort(arr.copy())

        elif choice == 5:
            result = sorting.quick_sort(arr.copy())

        elif choice == 6:
            result = sorting.heap_sort(arr.copy())

        elif choice == 7:
            result = sorting.shell_sort(arr.copy())

        elif choice == 8:
            result = sorting.counting_sort(arr.copy())

        elif choice == 9:
            result = sorting.radix_sort(arr.copy())

        elif choice == 10:
            result = sorting.bucket_sort(arr.copy())

        else:
            print("Invalid choice!")
            return

        print("\nSorted Array:")
        print(result)


# Program execution
if __name__ == "__main__":
    main = Main()
    main.run()