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
        
        for key,value in lended_books.items():
            if name_of_book_wanted == key:
               print(f"The Book is Not Available it is Lended to {value}")
            
        
        i = 0
        for item in self.listofbooks:
            if name_of_book_wanted == item:
                self.lended_books.update({self.name_of_book_wanted:self.nameofperson})
                del self.listofbooks[i]
                print(f"The Book is now lended to {nameofperson}")
            i +=1 
        
        
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
    
    mayankLib = Library(["subtle art of not giving a fuck","spectrum","laxmikant"],"Mayank Library")
    # book_add = input("Enter The Name of The Book Which you want to Donate!!!")
    # mayankLib.addBook(book_add)
    # print(mayankLib.listofbooks)
    lended_books = {"modern history":"mayank verma","majid hussain":"jitendra nirnejak"}
    mayankLib.lendBooks("spectrum","kitola",lended_books)
    print(mayankLib.lended_books)
    mayankLib.displayBooks()
    mayankLib.returnBook("spectrum")
    print(mayankLib.lended_books)
    mayankLib.displayBooks()
    # print(mayankLib.listofbooks)
    # print(mayankLib.lended_books)
    # print(mayankLib.lendBooks())
    # mayankLib.displayBooks()
