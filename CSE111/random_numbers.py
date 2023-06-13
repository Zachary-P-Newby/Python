from random import randint, uniform, choice

def main():
  numbers = [round(uniform(1,100),1), round(uniform(1,100),1), round(uniform(1,100),1)]
  print(f'numbers {numbers}')

  append_random_numbers(numbers)
  print(f'numbers {numbers}')

  append_random_numbers(numbers, 3)
  print(f'numbers {numbers}')


def append_random_numbers(numbers_list, quantity=1):
  for num in range(quantity):
    random_number = uniform(0, 100)
    rounded = round(random_number, 1)
    numbers_list.append(rounded)

  #return numbers_list

if __name__ == "__main__":
    main()
