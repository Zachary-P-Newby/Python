import csv

BYUI_INDEX = 0
NAME_INDEX = 1

def main():

  student_dictionary = read_dictionary("students.csv")
  #print(student_dictionary)
  byu_inumber = input("please enter your I-Number (xx-xxx-xxxx): ")
  byu_inumber = byu_inumber.replace("-", "")


  if not byu_inumber.isdigit():
    
    print("wrong character")
    
  else: 
    
    if len(byu_inumber) < 9:
      print("Invalid I-Number: too few digits")
  
    elif len(byu_inumber) > 9:
      print("Invalid I-Number: too many digits")

    else:
      if byu_inumber in student_dictionary:
        print(student_dictionary[byu_inumber])
      else:
        print("No such Student")



def read_dictionary(filename):
  """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """

  student_dictionary = {}

  with open(filename, mode="rt") as students:
    reader = csv.reader(students)

    next(reader)

    for line in reader:
      student_dictionary[line[BYUI_INDEX]] = line[NAME_INDEX]

  return student_dictionary


if __name__ == "__main__":
  main()
