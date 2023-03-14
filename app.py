from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField
from wtforms.validators import DataRequired
from logic import search_anime

SEARCH_MAIN = ''

app = Flask(__name__)
app.config['SECRET_KEY'] =  "nanashi@7011"

class NameForm(FlaskForm):
    name = StringField("Anime Name", validators=[DataRequired()])
    submit = SubmitField("Search")


@app.route("/", methods=['GET','POST'])
def hello_world():
    global SEARCH_MAIN
    name = None
    title = None
    gener = None
    image = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data   
        all_data = search_anime(name) 
        title = all_data[0]
        gener = all_data[1]
        image = all_data[2]
        form.name.data = " "
    return render_template("index.html", name=name, form=form , titles=title, geners=gener , images=image)

if __name__ == "__main__":
    app.run(debug=True)

# @app.errorhandler()

