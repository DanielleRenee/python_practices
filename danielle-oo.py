class Book(object):
    """A Book Object."""
    def __init__(self, title, author, pub_yr='Unknown'):
        self.title = title
        self.author = author
        self.pub_yr = pub_yr

    def __repr__(self):
        return '<Book. Title: %s.>' % (self.title)

class Library(object):
    """A collection of book objects."""

    def __init__(self):
        self.books = []

    def __repr__(self):
        print '<Library containing %s book(s).>' % (len(self.books))
        #Read up a bit more on dunder repr, notes for self:
        #A __repr__ method takes exactly one parameter, self, and must return a string. 
        #This string is intended to be a representation of the object, 
        #suitable for display to the programmer, 
        #for instance when working in the interactive interpreter. __repr__ 
        #will be called anytime the builtin repr function is applied to an object; 
        #this function is also called when the backquote operator is used.

    def list_books(self):
        """List all the books in the library."""

        if len(self.books) == 0:
            print "Library is empty."
            return
        for book in self.books:
            print book.title
            print '  Author:', book.author
            print '  Published:', book.pub_yr
            print

    def add_book(self, book):
        """Add a book to the library."""

        if not isinstance(book, Book):
            raise Exception('Please enter a Book Object to add to the library')
        self.books.append(book)
        print 'Added: {} by {}.'.format(book.title, book.author)

    def empty_library(self):
        """Remove all books from the library."""
        #if a library calls the empty_library method, clear all items from the library
        #tried clear method from python book, but found out clear wasn't added until 3.3
        #self.books.clear()
        #per stack overflow, searched for error message, used del instead 
        #https://stackoverflow.com/questions/32055768/python3-attributeerror-list-object-has-no-attribute-clear
        del self.books[:]
        print "Library deleted!"


########### WRITE YOUR SCRIPT HERE
# Details on what the script should include are in the skills assessment 
# instructions.

the_bell_jar = Book("The Bell Jar", "Sylvia", 1963)
# the_bell_jar.title = "The Bell Jar"
# the_bell_jar.author = "Sylvia Plath"
# the_bell_jar.pub_yr = 1963


anna_karenina = Book("Anna Karenina", "Leo Tolstoy")
# anna_karenina.title = "Anna Karenina"
# anna_karenina.author = "Leo Tolstoy"
# anna_karenina.pub_yr = "Unknown"

#sunday = Library()
#sunday.list_books = bound method Library.list_books of <Library containing 0 book(s)>
#sunday.add_book(the_bell_jar) #= Added: The Bell Jar
#sunday.add_book(anna_karenina) #= Added: Anna Karenina
#sunday.list_books() = 
# The Bell Jar
#   Author: Sylvia
#   Published: 1963

# Anna Karenina
#   Author: Leo Tolstoy
#   Published: Unknown

#sunday.empty_library() = Library deleted!
#sunday.list_books() = Library is empty.

#update the method add book. 
#sunday.add_book(the_bell_jar) = Added: The Bell Jar by Sylvia.















