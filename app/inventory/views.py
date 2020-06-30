from flask import flash, redirect, render_template, url_for

from . import inventory
from ..models import Books, Dvds, Cds
from .. import db
from .forms import BooksForm

@inventory.route('/inventory', methods=['GET', 'POST'])
def inventory_list():
    """
    Handle request to the /inventory route
    """

    return render_template('inventory/inventory.html', title='Inventory')

@inventory.route('/books', methods=['GET', 'POST'])
def books_list():
    """
    Handle request to books list
    """

    books = Books.query.all()

    return render_template('inventory/books/books_list.html', books=books, title='Books')

@inventory.route('/books/add', methods=['GET', 'POST'])
def books_add():
    """
    Handle request to add a book
    """

    form = BooksForm()
    if form.validate_on_submit():
        book = Books(id=form.code.data, b_title=form.title.data, b_publisher=form.publisher.data, b_shelf_id=form.shelf.data, b_quantity=form.quantity.data, b_language_id=form.language.data)

        try:
            # add book to the database
            db.session.add(book)
            db.session.commit()
            flash('You have successfully added a new book.')
        except:
            # in case book name already exists
            flash('Error: book name already exists.')

        # redirect to departments page
        return redirect(url_for('inventory.books_list'))

    return render_template('inventory/books/books_form.html', form=form, title='Add Book')    
