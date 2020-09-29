from flask import Flask, render_template, redirect, request

from app import app
from app import db

from models.models import Hexagon


@app.route("/")
def root():
    return redirect('/home')


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/hex/fetch", methods=["GET"])
def fetch_hex():
    inputname = request.form.get("hexname")
    book = Hexagon.query.filter_by(neighbor=inputname).first()
    print(book)
    # book.title = newtitle
    # db.session.commit()
    return redirect("/")


@app.route("/hex/create", methods=["GET", "POST"])
def create_hex():
    if request.form:
        print(request.form)
        return render_template("home.html")
    else:
        # name = request.form["name"]
        neighbor = request.form["neighbor"]
        border = request.form["border"]
        newHex = Hexagon(neighbor=neighbor, border=border)
        db.session.add(newHex)
        db.session.commit()
        # return render_template('create_hex.html')
        return redirect('/home')

# 
# @app.route('/', methods=['GET', 'POST'])
# def homepage():
#     if request.method == 'POST':
#         if request.form.get('content'):
#             # Create a new note in the db.
#             note = Note.create(content=request.form['content'])
# 
#             # Render a single note panel and return the HTML.
#             rendered = render_template('note3.html', note=note)
#             return jsonify({'note': rendered, 'success': True})
# 
#         # If there's no content, indicate a failure.
#         return jsonify({'success': False})
# 
#     notes = Note.public().limit(50)
#     return render_template('homepage.html', notes=notes)
# 
# 
# @app.route('/archive/<int:pk>/', methods=['POST'])
# def archive_note(pk):
#     try:
#         note = Note.get(Note.id == pk)
#     except Note.DoesNotExist:
#         abort(404)
#     note.archived = True
#     note.save()
#     return jsonify({'success': True})
