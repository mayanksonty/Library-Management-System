# Create a Library Class
# display books
# lend books - (maintain a dictionary who own the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks,library_name)

# dictionary (books - nameofperson) 

# create a main function and run a infinite while loop asking users for input 
 

class Library:
    def __init__(self,listofbooks,name_of_library):
        self.listofbooks = listofbooks
        self.name_of_library = name_of_library

    def displayBooks(self):
        print("Available books are as Follows\n")
        i = 0
        for item in self.listofbooks:
            print(f"{i+1} {item}")
            i +=1    

    def lendBooks(self,name_of_book_wanted,nameofperson,lended_books):
        self.lended_books = lended_books
        self.nameofperson = nameofperson
        self.name_of_book_wanted = name_of_book_wanted
        
        for key,value in self.lended_books.items():
            if self.name_of_book_wanted == key:
               print(f"The Book is Not Available it is Lended to {value}")
               return self.lended_books
            
        
        i = 0
        for item in self.listofbooks:
            if name_of_book_wanted == item:
                self.lended_books.update({self.name_of_book_wanted:self.nameofperson})
                del self.listofbooks[i]
                print(f"The Book is now lended to {nameofperson}")
                return self.lended_books
            i +=1 
        print(f"{self.name_of_book_wanted} book do not exist in the library try another Book Name")
        return self.lended_books
        
        
        # try:
        #     if lended_books[name_of_book_wanted]:
        #         print("book found")
        #     else:
        #         print(Error)
        # except Exception as e:
        #     print("Book not Found") 


    def addBook(self,name_of_book):
        self.name_of_book = name_of_book
        self.listofbooks.append(name_of_book)
        
        
    
    def returnBook(self,name_of_book_returned):
        self.name_of_book_returned = name_of_book_returned
        self.listofbooks.append(name_of_book_returned)
        del lended_books[name_of_book_returned]
        



if __name__ == '__main__':
    
    listofbooks = []
    lended_books = {}
    name_of_library = input("Enter the name of your Library ")
    number_of_books = int(input("How many books you want to Enter "))
   
    for i in range(number_of_books):
        listofbooks.append(input("Enter the Name of books your Library contains  "))
    
    while True:
        libraryInstance = Library(listofbooks,name_of_library)
        print(f"Welcome to {libraryInstance.name_of_library} Library !!!!!")
        user_input = int(input("Enter What you want to do\n1 = Donate Books\n2 = Return Books\n3 = Display all the Available books\n4 = get a book from Library "))

        if user_input == 1:
            name_of_book = input("Enter the Book Name which you want to donate ")
            libraryInstance.addBook(name_of_book)
        
        elif user_input == 2:
            name_of_book_returned = input("Name of the Book you Want to Return ")
            libraryInstance.returnBook(name_of_book_returned)
        
        elif user_input == 3:
            libraryInstance.displayBooks()
        
        elif user_input == 4:
            name_of_book_wanted = input("Enter the name of Book You wanted ")
            nameofperson = input("Enter Your Name ")
            lended_books = libraryInstance.lendBooks(name_of_book_wanted,nameofperson,lended_books)
        
        else:
            print("You have Entered Wrong Choice please choose from the above menu")



        # book_add = input("Enter The Name of The Book Which you want to Donate!!!")
        # mayankLib.addBook(book_add)
        # print(mayankLib.listofbooks)
        # lended_books = {"modern history":"mayank verma","majid hussain":"jitendra nirnejak"}
        # mayankLib.lendBooks("spectrum","kitola",lended_books)
        # print(mayankLib.lended_books)
        # mayankLib.displayBooks()
        # mayankLib.returnBook("spectrum")
        # print(mayankLib.lended_books)
        # mayankLib.displayBooks()
        # print(mayankLib.listofbooks)
        # print(mayankLib.lended_books)
        # print(mayankLib.lendBooks())
        # mayankLib.displayBooks()
