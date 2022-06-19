# Author: Yiğit Önder Ünver
# CENG1009: Programming Fundamentals Fall 2021 Project
# Library Project

class Book():
    def __init__(self, isbn, name, author, isChecked='F', checkers=[]):
        self.isbn = isbn
        self.name = name
        self.author = author
        self.isChecked = isChecked
        self.checkers = checkers

    def __str__(self):
        output = f"{self.isbn} | Name: {self.name} | Author: {self.author} | isChecked?: {self.isChecked}"
        if self.checkers:
            output += "\n         Checkers: "
            for checker in self.checkers:
                output += checker + ', '

        return output

class Student():
    def __init__(self, sId, name, books=[]):
        self.sId = sId
        self.name = name
        # [isbn, isbn, isbn]
        self.books = books
    
    def __str__(self):
        output = f"{self.sId} | Name: {self.name}"
        if self.books:
            output += "\n        Books: "
            for isbn in self.books:
                output += isbn + ', '
        
        return output




def displayCheckedBooks(books):
    """I: Displays checked books"""

    for book in books:
        if book.isChecked == 'T':
            print(book)

def displayBooks(books):
    """I: Displays all books"""

    for book in books:
        print(book)

def displayStudents(students):
    """I: Displays all students"""

    for student in students:
        print(student)

def displayTopBooks(books):
    """I: Displays top 3 books with most checkers"""

    booksCopy = books.copy()
    for i in range(3):
        max = booksCopy[0]
        for book in booksCopy[1:]:
            if len(book.checkers) > len(max.checkers):
                max = book
        booksCopy.remove(max)
        print(max)

def displayTopStudents(students):
    """I: Displays top 3 students with most book checks"""

    studentsCopy = students.copy()
    for i in range(3):
        max = studentsCopy[0]
        for student in studentsCopy[1:]:
            if len(student.books) > len(max.books):
                max = student
        studentsCopy.remove(max)
        print(max)




def searchBookByISBN(isbn, books)->Book:
    """Returns book object if isbn matches"""

    for book in books:
        if isbn == book.isbn:
            return book
    
    return None

def searchBookByName(name, books)->list:
    """Returns a book object whiches names matches name"""
    result = []

    for book in books:
        if name.lower() in book.name.lower():
            result.append(book)

    return result
    
def searchStudentById(sId, students)->Student:
    """Returns student object if id matches"""

    for student in students:
        if sId == student.sId:
            return student
    return None




def addBook(isbn, name, author, books):
    """Adds new book to books list"""
    if len(name) > 1 and len(isbn) > 1 and len(author) > 1:
        books.append(Book(isbn, name, author))
        print("Added book to database successfully.")
    else:
        print("Please fill in the informations properly.")

def checkOut(book, student):
    """Checks out book to a student"""

    if book != None and student != None:
        if book.isChecked == 'F':
            if book.isbn not in student.books:
                # Student
                student.books.append(book.isbn)

                # Book
                book.isChecked = 'T'
                book.checkers.append(student.sId)
                print("Checked successfully.")
            else:
                print("This book is already checked by this student.")
        else:
            print("This book is not available at the moment.")
    else:
        print("There is no such book or student logged to library.")

def checkIn(book):
    """Dechecks the book. Check not out, so check in :P"""

    if book != None:
        if book.isChecked == 'T':
            book.isChecked = 'F'
            print("Dechecked successfully.")
        else:
            print("This book is already available at the moment.")
    else:
        print("There is no such book.")




def loadDatabase(students, books):
    """Reads and prepares the data in database"""

    with open("students.txt", 'r') as file:
        for line in file.readlines():
            if ';' not in line:
                line += ';'
            student = line.split(';')[0].split()
            isbns = line.split(';')[1].split()
            students.append(  Student( student[0], ' '.join( student[1:] ), isbns)  )
            
    with open("books.txt", 'r') as file:
        for line in file.readlines():
            line = line.strip().split(',')
            books.append(  Book( line[0], line[1], line[2], line[3], line[4:] )  )

# Insert: Updating rather than rewriting is a must for optimization.
def saveDatabase(students, books):
    """Writes last changes to database."""

    with open("students.txt", 'w') as file:
        for student in students:
            output = f"{student.sId} {student.name};"
            for isbn in student.books:
                output += f" {isbn}"
            file.write(output + '\n')

    with open("books.txt", 'w') as file:
        for book in books:
            output = f"{book.isbn},{book.name},{book.author},{book.isChecked}"
            for sId in book.checkers:
                output += f",{sId}"
            file.write(output + '\n')




books = []
students = []

if __name__ == "__main__":
    loadDatabase(students, books)


    welcome = "\n-1) Exit.\n 0) Show this.\n 1) Add a new book.\n 2) Check out a book for student.\n 3) Decheck book.\n 4) Search a book by ISBN number.\n 5) Search a book by name.\n 6) List all the books in the library.\n 7) List all the books that are checked out.\n 8) List all the students.\n 9) List top 3 most checked out books.\n 10) List top 3 students with the highest checked out numbers."
    print(welcome)

    
    while 1:
        x = int(input("\nPlease insert action here: "))
        if  x==-1:  break
        elif x==0:  print(welcome)
        elif x==1:  
            isbn = input("Please enter ISBN of book: ")
            name = input("Please enter name of book: ")
            author = input("Please enter the author of book: ")
            # Checking for input format inside addBook function may not be the cleanest way
            addBook(isbn, name, author, books)
        elif x==2:  
            isbn = input("Please enter ISBN of book: ")
            sId = input("Please enter ID of student: ")
            checkOut(searchBookByISBN(isbn, books), searchStudentById(sId, students))
        elif x==3:
            isbn = input("Please enter ISBN of book: ")
            checkIn(searchBookByISBN(isbn, books))
        elif x==4:
            isbn = input("Please enter ISBN of book: ")
            print(searchBookByISBN(isbn, books))
        elif x==5:
            name = input("Please enter name of book: ")
            for book in searchBookByName(name, books):
                print(book)
        elif x==6:  displayBooks(books)
        elif x==7:  displayCheckedBooks(books)
        elif x==8:  displayStudents(students)
        elif x==9:  displayTopBooks(books)
        elif x==10: displayTopStudents(students)
        else:       print("\nThere is no such operation.")


    saveDatabase(students, books)