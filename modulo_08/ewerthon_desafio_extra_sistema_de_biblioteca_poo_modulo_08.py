class Books:
    def __init__(self, title, type, author):
        self.title = title
        self.author = author
        self.type = type
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} - {self.author} ({status})"

class Library:
    def __init__(self):
        self.books = []
    
    def add_books(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
    
    def borrowed_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"You borrowed the book: {book.title}")
                return
        print("Book unavailable or not found")
    
    def giveBack_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"You give back the book: {book.title}")
                return
        print("Book find or its already available ")


biblioteca = Library()

l1 = Books("Dom Casmurro", "Machado de Assis", "Education")
l2 = Books("1984", "George Orwell", "Terror")

biblioteca.add_books(l1)
biblioteca.add_books(l2)
print("-------------------------")
biblioteca.list_books()
print("-------------------------")
biblioteca.borrowed_book("1984")
print("-------------------------")
biblioteca.list_books()
print("-------------------------")
biblioteca.giveBack_book("1984")
print("-------------------------")
biblioteca.list_books()
