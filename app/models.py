from app import db

class Books(db.Model):
    """
    Create a Books table
    """

    __tablename__ = 'books'

    id = db.Column(db.String(20), primary_key=True)
    b_title = db.Column(db.String(30))
    b_publisher = db.Column(db.String(30))
    b_shelf_id = db.Column(db.Integer, db.ForeignKey('shelf.id'))
    b_quantity = db.Column(db.Integer)
    b_language_id = db.Column(db.Integer, db.ForeignKey('language.id'))

    def __repr__(self):
        return '<Book: {}>'.format(self.b_title)

class Dvds(db.Model):
    """
    Create a DVDs table
    """

    __tablename__ = 'dvds'

    id = db.Column(db.String(20), primary_key=True)
    d_title = db.Column(db.String(30))
    d_shelf_id = db.Column(db.Integer, db.ForeignKey('shelf.id'))
    d_quantity = db.Column(db.Integer)
    d_language_id = db.Column(db.Integer, db.ForeignKey('language.id'))
    def __repr__(self):
        return '<Dvd: {}>'.format(self.d_title)

class Cds(db.Model):
    """
    Create a CDs table
    """

    __tablename__ = 'cds'

    id = db.Column(db.String(20), primary_key=True)
    c_title = db.Column(db.String(30))
    c_shelf_id = db.Column(db.Integer, db.ForeignKey('shelf.id'))
    c_quantity = db.Column(db.Integer)
    c_language_id = db.Column(db.Integer, db.ForeignKey('language.id'))

    def __repr__(self):
        return '<Cd: {}>'.format(self.c_title)

class Language(db.Model):
    """
    Create a Language table
    """

    __tablename__ = 'language'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    books = db.relationship('Books', backref='language', lazy='dynamic')
    dvds = db.relationship('Dvds', backref='language', lazy='dynamic')
    cds = db.relationship('Cds', backref='language', lazy='dynamic')
    def __repr__(self):
        return '<Language: {}>'.format(self.name)

class Shelf(db.Model):
    """
    Create a Shelf table
    """

    __tablename__ = 'shelf'

    id = db.Column(db.Integer, primary_key=True)
    sh_desc = db.Column(db.String(10), unique=True)
    books = db.relationship('Books', backref='shelf', lazy='dynamic')
    dvds = db.relationship('Dvds', backref='shelf', lazy='dynamic')
    cds = db.relationship('Cds', backref='shelf', lazy='dynamic')

    def __repr__(self):
        return '<Shelf: {}>'.format(self.sh_desc)