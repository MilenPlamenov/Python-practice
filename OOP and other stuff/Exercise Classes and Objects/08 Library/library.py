class Library:
    def __init__(self):
        self.user_records = []  # store the users
        self.books_available = {}  # store the key - author with value list of books available for each of the authors
        self.rented_books = {}  # usernames - key and value - dictionary with books as a kay and days left before return

    def get_book(self, author, book_name, days_to_return, user):
        if book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username].update({book_name: days_to_return})
            user.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for user, books in self.rented_books.items():
            for book, time in books.items():
                if book == book_name:
                    return f'The book "{book_name}" is already rented and will be available in {time} days!'

    def return_book(self, author, book_name, user):
        if book_name in user.books:
            user.books.remove(book_name)
            self.rented_books[user.username].pop(book_name)
            self.books_available[author].append(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"

