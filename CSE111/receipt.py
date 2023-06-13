import csv, datetime

def main():
    try:
        #create key-column index
        key_column_index = 0

#create dict
        product_dict = read_dictionary("C:\\Users\\zpnew\\OneDrive\\byu-idaho\\CSE111\\products.csv",key_column_index)

#print products
    #print(f"All products: {product_dict}")

#open request.csv and convert to order list
        with open("C:\\Users\\zpnew\\OneDrive\\byu-idaho\\CSE111\\request.csv", mode = "rt") as request:
            request_reader = csv.reader(request)
        
            next(request_reader)

            order = []

            for item in request_reader:
                current_key = item[0]
                order.append([product_dict[current_key], item[1]])


#run script

        taxrate = .06

        print_receipt(order, taxrate)

#____________________________________________________________________________
#exception handling
    except FileNotFoundError:
        print("Error: missing file\n[Errno 2] No such file or directory: 'products.csv'")
    
    except PermissionError:
        print("Error: No Permissions\nUnable to access file, you need to gain permission to access the file")
    
    except KeyError :
        print(f"Error: unknown product ID in the request.csv file \n '{current_key}'")

#_______________________________________________________________________________

def read_dictionary(filename, key_column_index, print_index = False):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    #create dict to store products
    product_dict = {}
    #open file and add products to dictionary
    with open(filename, mode = "rt") as products_file:

        next(products_file)
        
        #make reader
        reader = csv.reader(products_file)

        dict_index = {}

        #for loop that goes through products and adds them to list
        for item in reader:
            key_column_index +=1
            product_dict[item[0]] = item[1::]
            dict_index[item[0]] = key_column_index
    
    if print_index:
        print(f"Product index: {dict_index}")
    
    return product_dict
            

#_______________________________________________________________________

def print_receipt(order, taxrate = 0):
    """
Prints a receipt for the order with prices taken form the product dictionary
Then it prints the totals and calculates the sales tax
Input:
    order: list
    tax: float (.10, .45, .345, etc)
Output: None
    """
    #starting values
    subtotal = 0
    item_count = 0

    current_date_and_time = datetime.datetime.now()

    print("")
#Store name
    print("Ruby Mart\n")
#print order
    print("Ordered Items:\n")
    
    for product in order:
        #print items
        print(f"{product[0][0]}: {product[1]} @ {product[0][1]}")
        
        #change variables
        items = int(product[1])
        item_count += items
        subtotal += float(product[0][1]) * items

#calcualte tax:
    tax = subtotal * taxrate
    total = subtotal + tax

#Print toatals
    print("")
    print(f"Number of items: {item_count}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {tax:.2f}")
    print(f"Total: {total:.2f}")
    print("")

    #finish receipt
    print("Thank you for shopping at Ruby Co.")
    print(f"{current_date_and_time:%A %b %d %I:%M %p :%Y}")
    


if __name__ == "__main__":
    main()