#Define Variables
most_chapters = 0
largest_book = ""

#Open the file
with open("books_and_chapters.txt") as books_and_chapters:
    #Process Data
    for book in books_and_chapters:
        book = book.split(":")
        chapters = int(book[1])

        if chapters >= most_chapters:
            most_chapters = chapters
            largest_book = book
        else:
            pass

        print(f"Scripture: {book[2]}, Book: {book[0]}, chapters: {book[1]}")

    print(f"The largest book is {largest_book[0]}, with {most_chapters} chapters.")