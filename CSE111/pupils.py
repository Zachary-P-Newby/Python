import csv

# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2


def main():
  try:
    #open and read pupils.csv
    pupils_raw_list = read_compound_list("C:\\Users\\zpnew\\OneDrive\\byu-idaho\\CSE111\\pupils.csv")

    sort_by_birthyear(pupils_raw_list)

    sort_given_name(pupils_raw_list)

    sort_by_birth_month_and_day(pupils_raw_list)

  except (FileNotFoundError, PermissionError) as error:
    print(f"{error} has occurred. Please fix this.")

  finally:
    print('finished!')


def sort_by_birthyear(pupils_raw_list):
  #create lambda
  birthdate = lambda student: student[BIRTHDATE_INDEX]
  #process list
  pupils_sorted = sorted(pupils_raw_list, key=birthdate)
  #output list to screen
  print('Birth Year Sorted List')
  print("")
  print_list(pupils_sorted)
  print("")


def sort_given_name(pupils_raw_list):
  #create lambda
  given_name = lambda student: student[GIVEN_NAME_INDEX]
  #process list
  pupils_sorted = sorted(pupils_raw_list, key=given_name)
  #output list to screen
  print('Given Name Sorted List')
  print()
  print_list(pupils_sorted)


def sort_by_birth_month_and_day(pupils_raw_list):
  #create lambda
  birthdate = lambda student: student[BIRTHDATE_INDEX][5::]
  #process list
  pupils_sorted = sorted(pupils_raw_list, key=birthdate)
  #output list to screen
  print('Birth Month and day Sorted List')
  print("")
  print_list(pupils_sorted)
  print("")


def read_compound_list(filename):
  """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
  # Create an empty list.
  compound_list = []

  # Open the CSV file for reading.
  with open(filename, "rt") as csv_file:

    # Use the csv module to create a reader
    # object that will read from the opened file.
    reader = csv.reader(csv_file)

    # The first line of the CSV file contains column headings
    # and not a student's I-Number and name, so this statement
    # skips the first line of the CSV file.
    next(reader)

    # Process each row in the CSV file.
    for row in reader:

      # Append the current row at the end of the compound list.
      compound_list.append(row)

  return compound_list


def print_list(compound_list):
  for item in compound_list:
    print(item)


if __name__ == "__main__":
  main()
