from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory data (you can replace with a database later)
books = [
    {"id": 1, "title": "Python Basics", "author": "John Doe", "available": True},
    {"id": 2, "title": "Data Science 101", "author": "Jane Smith", "available": True}
]
next_id = 3

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add():
    global next_id
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        books.append({"id": next_id, "title": title, "author": author, "available": True})
        next_id += 1
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/borrow/<int:book_id>')
def borrow(book_id):
    for book in books:
        if book['id'] == book_id and book['available']:
            book['available'] = False
            break
    return redirect(url_for('index'))

@app.route('/return/<int:book_id>')
def return_book(book_id):
    for book in books:
        if book['id'] == book_id and not book['available']:
            book['available'] = True
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
