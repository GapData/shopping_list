import re
from flask import Flask, request, redirect, url_for, render_template, session, flash
from stringdb import create, get_items, remove_item

app = Flask(__name__)
app.secret_key = "hai!sdflkasfalskdfjw33"

#students = []


@app.route('/')
def root():
    return redirect(url_for('index'))


@app.route('/shopping_list', methods=['GET', 'POST'])
def index():
    """lyst is the string representing the data. It is stored in the session as 'lyst'."""
    if 'lyst' in session:
        lyst = session['lyst']
    else:
        lyst = ''
    if request.method == 'POST':
        item = request.form['item']
        # remove html tags from field
        item = re.sub("<.*?>", "", item)
        session['lyst'] = create(item, lyst)
        return redirect(url_for('index'))
    items = get_items(lyst)
    return render_template('index.html', items=items)


@app.route('/shopping_list/new')
def new():
    return render_template('new.html')


@app.route('/shopping_list/<item>/delete', methods=['POST'])
def delete(item):
    if 'lyst' in session:
        lyst = session['lyst']
        session['lyst'] = remove_item(item, lyst)
        flash("item deleted.")
    else:
        flash("item not in list")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=3000)
