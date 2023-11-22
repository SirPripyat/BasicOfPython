def binary_search(array: list[str], left, right, item_to_search):

  middle = (left + right) // 2

  if item_to_search == array[middle]: return f"Item {item_to_search} encontrado na posição: {middle}"
 
  if array[middle] > item_to_search:
    # go to left part of the array
    return binary_search(array, left, middle - 1, item_to_search)
  
  if array[middle] < item_to_search: 
    # go to right part of the array
    return binary_search(array, middle + 1, right, item_to_search)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(binary_search(array, 0, len(array), 7))