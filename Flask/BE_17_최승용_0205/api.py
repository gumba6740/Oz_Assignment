from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema


blp = Blueprint('books', 'books', url_prefix='/books', description="Operations on books")

books = []
id = 1

def find_one(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        abort(404, message="Book not found")
    return book

@blp.route("/")
class BookList(MethodView):

    @blp.response(200, BookSchema(many=True))
    def get(self):
        return books
    
    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def post(self, new_data):
        global id
        new_data["id"] = id
        id += 1
        books.append(new_data)
        return new_data
    
@blp.route("/<int:book_id>")
class Book(MethodView):

    @blp.response(200, BookSchema)
    def get(self, book_id):
        return find_one(book_id)
    
    @blp.arguments(BookSchema)
    @blp.response(200, BookSchema)
    def put(self, new_data, book_id):
        book = find_one(book_id)
        book.update(new_data)
        return book

    @blp.response(204)
    def delete(self, book_id):
        global books
        book = find_one(book_id)
        books.remove(book)