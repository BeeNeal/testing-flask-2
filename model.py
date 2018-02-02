from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))

def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

# How do we check that this was written correctly before running tests with it?
def example_data():
    """Create example data for the test database."""

    viticulture = Game(name='Viticulture', description='A game about winemaking')
    dixit = Game(name='Dixit', description='Like CAH but with pictures')
    cytosis = Game(name='Cytosis', description='Worker placement with Bio')

    # .add_all() Takes a list of objects
    db.session.add_all([viticulture, dixit, cytosis])
    db.session.commit()


if __name__ == '__main__':
    from server import app
    # Remember to remove second arg when done testing.
    connect_to_db(app)
    print "Connected to DB."
