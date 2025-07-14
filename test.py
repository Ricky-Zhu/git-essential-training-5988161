def select_positive_odd_numbers_less_than(n):
  """
  Returns a list of positive odd numbers less than n.
  """
  return [x for x in range(1, n) if x % 2 == 1]


print(select_positive_odd_numbers_less_than(10))  # Output: [1, 3, 5, 7, 9]