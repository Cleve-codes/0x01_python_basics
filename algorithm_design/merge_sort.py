def merge_sort(array):
  # Get the middle point of the array
  middle_point = len(array) // 2

  # Split the array into two halves
  left_half = array[:middle_point]
  right_half = array[middle_point:]

  # Recursively sort the two halves
  merge_sort(left_half)
  merge_sort(right_half)

  left_half_index = right_half_index = merged_index = 0

  # Merge the two halves
  while left_half_index < len(left_half) and right_half_index < len(right_half):
    if left_half[left_half_index] < right_half[right_half_index]:
      array[merged_index] = left_half[left_half_index]
      left_half_index += 1
    else:
      array[merged_index] = right_half[right_half_index]
      right_half_index += 1
    merged_index += 1