from flask import render_template, redirect, url_for
from app import app
from app.scripts import *

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    action = request.args.get('act')
    if(action == '1'):
        addBook()
        return redirect(url_for('dashboard'))
    elif(action == '2'):
        addAssoc()
        return redirect(url_for('dashboard'))
    elif(action == '3'):
        addWh()
        return redirect(url_for('dashboard'))
    elif(action == '4'):
        addPrint()
        return redirect(url_for('dashboard'))
    elif(action == '5'):
        addClient()
        return redirect(url_for('dashboard'))

    pub.commit()
    authors = getAuths()
    editors = getEds()
    illustrators = getIlls()
    translators = getTrans()
    mycats = getCategories()
    return render_template("dashboard.html",
                           authors=authors,
                           editors=editors,
                           illustrators=illustrators,
                           translators=translators,
                           cats=mycats)

@app.route('/book', methods=['GET', 'POST'])
def book():
    pub.commit()
    bkid = request.args.get('bkid')
    mybook,mykeys = searchFull(bkid)
    return render_template("book.html", keys = mykeys, attrs=mybook, number = len(mybook))


@app.route('/', methods=['GET', 'POST'])
def index():
    pub.commit()
    text = ""
    cat = 0
    try:
        text = request.form['keyword']
        cat = request.form['categories']
    except:
        pass

    myBooks, mykeys, myids  = searchbooks(text,cat)
    mycats = getCategories()
    return render_template('index.html', books=zip(myBooks,myids), keys=mykeys, cats = mycats)
