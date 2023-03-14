from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField
from wtforms.validators import DataRequired

SEARCH_MAIN = ''

app = Flask(__name__)
app.config['SECRET_KEY'] =  "nanashi@7011"

class NameForm(FlaskForm):
    name = StringField("What's Your name", validators=[DataRequired()])
    submit = SubmitField("Search")


@app.route("/", methods=['GET','POST'])
def hello_world():
    global SEARCH_MAIN
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data    
        form.name.data = " "
    return render_template("index.html", name=name, form=form)

if __name__ == "__main__":
    app.run(debug=True)

# @app.errorhandler()

