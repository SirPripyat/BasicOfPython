def bubble_sort(array: list[str]):

    for pass_number in range(len(array) - 1, 0, -1):
        for i in range(pass_number):
            if array[i] > array[i + 1]:
              temporary = array[i]
              array[i] = array[i + 1]
              array[i + 1] = temporary
      
array_for_test = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(array_for_test)

print(array_for_test)

