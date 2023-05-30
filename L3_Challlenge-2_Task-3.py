def min_and_max(list):
  list_to_return = []
  lowest_value = list[0]
  highest_value = list[0]
  for number in list:
    if number > highest_value:
      highest_value = number
      continue
    elif number < lowest_value:
      lowest_value = number
      continue
    else:
      continue
  list_to_return.append(lowest_value)
  list_to_return.append(highest_value)
  return list_to_return

print(min_and_max([-2, 20, 4, 7, -10]))