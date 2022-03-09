from flask import Flask, redirect, render_template

app = Flask(__name__)
# app.secret_key = 'allo'
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'
# app.config['USE_SESSION_FOR_NEXT'] = True
# app.config["SQLALCHEMY_DATABASE_URI"] = r"sqlite:///templates/static/data/users2.sqlite"
# db = SQLAlchemy(app)
# class DBUser(db.Model):
#     __tablename__ = 'users'
#     username = db.Column(db.Text(), primary_key=True)
#     email = db.Column(db.Text(), nullable=False)
#     phone = db.Column(db.Text())
#     password = db.Column(db.Text(), nullable=False)
#
#     def __repr__(self):
#         return "<User {}: {} {}>".format(self.username, self.email, self.phone)


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/heroes')
def heroes():
    return render_template('heroes.html')

@app.route('/society')
def society():
    return render_template('jump.html')


@app.route('/About_Game')
def about_game():
    return render_template('About_Game.html')

@app.route('/register')
def register():
    return render_template('registerforgame.html')



if __name__ == '__main__':
    app.run()
