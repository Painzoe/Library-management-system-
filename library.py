book_types = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
]
book_list = [[] for _ in range(len(book_types))]
menu = """
 ------ Menu ------
 1. Add a book
 2. Remove a book 
 3. Show all books
 4. Exit
"""
print(menu)
while True:
    option = input("Please choose an option: ")
    if option == "1":
        type= """
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
        print(type)
        book_type = int(input("Select a book type number that suits your book: "))
        book = input("Enter the book name that you want to add: ")
        book_list += [book_type][book]
        print("Book added!")

    elif option == "2":
        book_to_remove = input("Enter the book name that you want to remove from the library or if you want to remove all books, write \"remove\": ")
        if book_to_remove == "remove":
            book_list.clear()
        else:
            if book_to_remove in book_list:
                book_list.remove(book_to_remove)
                print("Book removed!")
            else:
                print("The book does not exist!")
    elif option == "3":
        if len(book_list) == 0:
            print("There is no books in the library!")
        else:
            print("""
            1. View a certain type of books 
            2. View all books
            """)
            choice = int(input("Please make a choice: "))
            if choice == 1:
                book_type = int(input("Which type of book list do you want to view: "))
                for i in range(len(book_list[book_type])):
                    print(book_list[book_type][i])
            elif choice == 2:
                print("All books in the library: ")
                for i in range(len(book_list)):
                    print(i+1,".", book_list[i])
            else:
                print("Your choice is not valid!")

    elif option == "4":
        exit()
    else :
        print("Invalid option!")


