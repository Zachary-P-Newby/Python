def main():
    try:
        # Open the file phone_numbers.txt for reading and read all
        # of the phone numbers into a list named phone_numbers.
        phone_numbers = read_list("C:\\Users\\zpnew\\OneDrive\\byu-idaho\\CSE111\\phone_numbers.txt")

        # Print the list of phone numbers which will show that
        # some of the phone number don't have an area code.
        print(phone_numbers)

        # Some of the phone numbers in phone_numbers.txt do not start
        # with an area code. Replace each short phone number with a
        # phone number that begins with the area code "208-" To do this,
        # call the map function and pass the add_area_code function and
        # the list of phone numbers as arguments to the map function.
        nums = map(add_area_code,phone_numbers)
        new_numbers = []

        for item in nums:
            new_numbers.append(item)

        # Print the list with the corrected phone numbers.
        print(new_numbers)

    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")


def add_area_code(phone_number):
    """Phone numbers in the U.S. are often stored as ten digits and
    two dashes in this format: "ddd-ddd-dddd" where each d is a digit.
    If the length of phone_number is less than 12 characters, add the
    area code "208-" at the beginning of phone_number and return
    phone_number.

    Parameter phone_number: a string of digits formatted as
        "ddd-dddd" or "ddd-ddd-dddd"
    Return: a string of digits formated as "ddd-ddd-dddd"
    """
    if len(phone_number) < 12:
        phone_number = "208-" + phone_number
    else:
        pass

    return phone_number


def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list named text_list.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)

    # Return the list that contains the lines of text.
    return text_list



def test_number_maker():
    nums = ['208-318-1623', '208-384-7712', '986-314-1378', '307-377-4921',
 '208-671-7536', '986-228-7414', '208-693-6706', '208-274-2098',
 '208-854-3221', '208-361-9817', '208-422-3492', '208-631-1374',
 '986-533-9667', '208-158-9497', '208-892-9830', '208-477-5323',
 '406-204-8756', '208-805-2538', '208-913-9942', '208-216-9589',
 '406-138-9226', '801-644-6761', '208-814-4444', '208-822-6738',
 '208-892-1093', '208-936-6389', '435-656-5821', '435-605-8294',
 '208-271-1868', '208-894-6391', '208-232-4118', '208-132-2121',
 '208-515-8227', '208-848-2334', '208-426-1557', '208-952-4330',
 '208-998-2171', '208-743-9219', '208-944-4381', '208-589-7767',
 '208-407-3555', '208-928-9293', '208-957-5808', '208-940-6629',
 '208-825-9259', '208-123-7580', '208-374-8128', '208-847-4807',
 '986-159-8293', '208-515-9963', '406-241-6676', '208-907-1851',
 '208-297-6367', '208-936-8173', '208-376-7010', '208-681-1558',
 '208-800-4436', '208-590-8866', '208-788-1866', '208-163-7631',
 '208-928-8793', '406-595-2898', '208-330-3155', '208-884-7294',
 '208-120-4949', '801-343-8776', '208-362-3779', '208-482-2107',
 '208-366-5618', '435-957-8250', '208-441-5628', '307-494-6001',
 '208-571-5297', '208-366-7389', '801-730-8010', '208-134-6240',
 '208-402-3658', '208-151-9828', '208-485-7973', '208-506-2683',
 '208-518-9635', '208-769-7551', '208-776-1574', '208-604-4304',
 '208-119-9734', '208-917-6174', '208-773-1167', '307-749-5991',
 '208-334-8971', '208-995-8602', '208-193-5073', '208-345-4015',
 '208-367-8633', '208-289-6515', '208-265-8998', '208-800-3565',
 '208-211-2706', '208-408-3950', '208-928-3119', '208-691-9409']
    
    return nums

# If this file is executed like this:
# > python add_area_code.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
