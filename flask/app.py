from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '{"ENTER DB_URI"}/users'


db=SQLAlchemy(app)
class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(40))
    lname=db.Column(db.String(40))
    pet=db.Column(db.String(40))

    def __init__(self, fname, lname, pet):
        self.fname=fname
        self.lname=lname
        self.pet=pet

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method =='POST':
        fname= request.form['fname']
        lname= request.form['lname']
        pet= request.form['pets']

        user=User(fname, lname, pet)
        db.session.add(user)
        db.session.commit()
    
    return render_template('success.html', data=fname)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)