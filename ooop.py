# Base class
class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self._pages = pages  # encapsulated (protected)

    def display_info(self):
        print(f"📘 '{self.title}' by {self.author} - {self.genre}, {self._pages} pages")

    def read(self):
        print(f"Reading '{self.title}'... 📖")

# Derived class
class EBook(Book):
    def __init__(self, title, author, genre, pages, file_format, file_size):
        super().__init__(title, author, genre, pages)
        self.file_format = file_format
        self.file_size = file_size

    def display_info(self):
        super().display_info()
        print(f"Format: {self.file_format}, Size: {self.file_size}MB 💾")

    def download(self):
        print(f"Downloading '{self.title}' in {self.file_format} format... ⬇️")

# Example usage
physical_book = Book("1984", "George Orwell", "Dystopian", 328)
ebook = EBook("Digital Fortress", "Dan Brown", "Thriller", 356, "PDF", 5)

physical_book.display_info()
physical_book.read()
print()
ebook.display_info()
ebook.read()
ebook.download()
