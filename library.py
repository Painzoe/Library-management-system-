book_types = {
    1  : "Fiction" ,
    2  : "Non-Fiction" ,
    3  : "Fantasy" ,
    4  : "Sci-Fi" ,
    5  : "Mystery/Thriller" ,
    6  : "Romance" ,
    7  : "Horror" ,
    8  : "Biography/Autobiography" ,
    9  : "Self-Help" ,
    10 : "Classics"  ,
    }

book_list = [[] for _ in range(len(book_types))]
menu = """
 ------ Menu ------
 1. Add a book 
 2. Remove a book / Remove books 
 3. View books
 4. Exit
"""

genres = """
------ Book Genres ------
1. Fiction – Made-up stories 
2. Non-Fiction – Fact-based 
3. Fantasy – Magic, mythical worlds 
4. Science Fiction (Sci-Fi) – Futuristic tech, space 
5. Mystery/Thriller – Crime, suspense, detectives 
6. Romance – Love stories
7. Horror – Scary, supernatural 
8. Biography/Autobiography – Real-life stories 
9. Self-Help – Personal growth, motivation
10. Classics – Timeless literature
"""
def file_read(file_name,booklist):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                cleanedline = line.strip()
                if ":" in cleanedline:
                    genre_part, books_part = cleanedline.split(":",1)
                    for number, genre in book_types.items():
                        if genre == genre_part:
                            for book in books_part.split(","):
                                booklist[number - 1].append(book.strip())
    except FileNotFoundError:
        pass

def file_update(file_name, booklist):
        with open(file_name,"w", encoding="utf-8") as file:
            for i,genre in enumerate(booklist):
                if genre: #if it is empty,do not write
                    file.write(f"{book_types[i + 1]}:")
                    file.write(",".join(genre))
                    file.write("\n")

file_read("MyLibrary.txt",book_list)
while True:
    print(menu)
    option = input("Please choose an option: ")
    if option == "1":
        print(genres)
        book_type = int(input("Select a book type number that suits your book: "))
        book = input("Enter the book name that you want to add: ").lower()
        book_list[book_type - 1].append(book)
        print("Book added!")
        file_update("MyLibrary.txt", book_list)

    elif option == "2" :
        remove = """
        ------ remove options ------
        1. Remove a book
        2. Remove all books in a certain type 
        3. Remove all books in the library
        """
        print(remove)
        choice = input("Please choose an option: ")
        if choice == "1":
            book_to_remove = input("Enter the book name that you want to remove: ").lower()
            for i in range(10):
                if book_to_remove in book_list[i]:
                    book_list[i].remove(book_to_remove)
                    print("Book removed!")
                    file_update("MyLibrary.txt", book_list)
                    break
            else : print("Book not found!")
        elif choice == "2":
            print(genres)
            genre_to_remove = int(input("Enter the genre number to remove: "))
            book_list[genre_to_remove - 1].clear()
            file_update("MyLibrary.txt", book_list)
        elif choice == "3":
            for i in range(len(book_list)):
                book_list[i].clear()
            print("All books removed!")
            file_update("MyLibrary.txt", book_list)
        else:
            print("Invalid option!")

    elif option == "3":
        books = """
        ------ Viewing options ------
        1.View a certain type of books
        2.View all books        
        """
        print(books)
        choice = input("Please choose an option: ")
        if choice == "1":
            print(genres)
            genre_to_show = int(input("Enter the genre number to show: "))
            print(book_types[genre_to_show],"Books List:",book_list[genre_to_show - 1])
        elif choice == "2":
            for i in range(len(book_list)):
                print((i +1),")",book_types[i+1],"Books List:",book_list[i])
        else:
            print("Invalid option!")

    elif option == "4":
        exit()
    else :
        print("Invalid option!")
    enter = input("Press enter to continue...")