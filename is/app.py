import sqlite3
from flask import Flask , render_template,request

app = Flask(__name__)

@app.route('/') #Navn på start siden url
#@app.route('/home')
def home():
    return render_template ('index.html')


#navn på ing bliver ikke vist efter mellem rum 
@app.route('/ingEdit',  methods=['GET', 'POST'])
def editING():
    con = sqlite3.connect("/Users/win/Desktop/is/butikken.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    q = "select * from ingredienser"
    cur.execute(q)
    rows = cur.fetchall()


    if request.method == "POST":
        qid__input = request.form["qid__input"]
        qedit_input_navn = request.form["qedit_input_navn"]
        qedit_inventory = request.form["qedit_inventory"]

        con = sqlite3.connect("/Users/win/Desktop/is/butikken.db")
        cur = con.cursor()
        rows = cur.fetchall()

        print(qedit_inventory)
        print(qedit_input_navn) 
    
        cur.execute("UPDATE ingredienser SET "
        + "navnING='" + qedit_input_navn + "' , "
        + "inventar='" + qedit_inventory
        +"' WHERE idIngredienser = '"+ qid__input+"'")

        con.commit()
        return render_template("nyedit_ing.html")

    return render_template("ingEdit.html",rows=rows)


#add ing 
@app.route('/add',  methods=['GET', 'POST'])
def add():

    con = sqlite3.connect("/Users/win/Desktop/is/butikken.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute("""select * from ingredienser  """)
    rows = cur.fetchall()
    cur.close()
    con.close()
    if request.method == "POST":
        navn_html = request.form["ingre_input_navn"]
        inventory1 = request.form["inventory"]
      
        print(navn_html) #værdigerne fra html input
        print(inventory1)#variablen blive kun brugt her nu
        sqliteConnection = sqlite3.connect('/Users/win/Desktop/is/butikken.db')
        cursor = sqliteConnection.cursor()

        sqlite_insert_query = """INSERT INTO ingredienser (navnING, inventar) VALUES  (?,?)"""
        data = (str(navn_html), inventory1)

        print("row værdi: ", data)
        cursor.execute(sqlite_insert_query, data)

        sqliteConnection.commit()
     
        return render_template("flot.html")     
   
    return render_template("add.html",rows=rows)

# fejl side
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('error.html')


#edit iS
@app.route('/edit',  methods=['GET', 'POST'])
def edit():
    con = sqlite3.connect("/Users/win/Desktop/is/butikken.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Ice ")
    rows = cur.fetchall()
    con.close()
    if request.method == "POST":
        qis_id = request.form["is_id"]
        qis_navn = request.form["is_navn"]
    
        con = sqlite3.connect("/Users/win/Desktop/is/butikken.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        print(qis_id)
        print(qis_navn)
        cur.execute("UPDATE Ice SET "
        + "navn='" + qis_navn
        +"' WHERE idIs = '"+ qis_id+"'")      
        con.commit()
        return render_template('t_is_edit.html',rows = rows)


    return render_template('edit.html',rows = rows)



@app.route('/nyedit_ing',  methods=['GET', 'POST'])
def nyedit():
    con = sqlite3.connect("/Users/win/Desktop/is/butikken.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    q = "select * from ingredienser "
    cur.execute(q)
    rows = cur.fetchall()


    return render_template("nyedit_ing.html", rows = rows )


@app.route('/vis_ingredienser') #Navn på start siden url
def vis_ingredienser():
    con = sqlite3.connect("/Users/win/Desktop/is/butikken.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from ingredienser ")
    rows = cur.fetchall()
    con.close()

    return render_template ('vis_ingredienser.html',rows = rows)

@app.route('/is_oversigt') #Navn på start siden url
def is_oversigt():
    con = sqlite3.connect("/Users/win/Desktop/is/butikken.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Ice ")
    rows = cur.fetchall()
    con.close()

    return render_template ('is_oversigt.html',rows = rows)


@app.route('/lavis',  methods=['GET', 'POST'])
def lavis():

    if request.method == "POST":
        skrive_input = request.form["is_pro"]
        print(skrive_input)
       
        con = sqlite3.connect("/Users/win/Desktop/is/butikken.db")
        cur = con.cursor()

        w = ("""UPDATE ingredienser set inventar = inventar - forbindelse.mængde FROM forbindelse 
            WHERE ingredienser.idIngredienser = forbindelse.fkingredienser AND
                        fkis = (?) """)

        cur.execute(w , [skrive_input])
        con.commit()
        con.close()

        return render_template("insenerlavet.html"  )
        
    else:
        con = sqlite3.connect("/Users/win/Desktop/is/butikken.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        sqll = """SELECT * from ice """
        cur.execute(sqll)

        rows = cur.fetchall()

        con.commit()
        cur.close()
        return render_template("lavis.html",rows=rows)


@app.route('/delete',  methods=['GET', 'POST'])
def delete():
    con = sqlite3.connect("/Users/win/Desktop/is/butikken.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute("""select * from ingredienser  """)
    rows = cur.fetchall()
    #cur.close()
    #con.close()
    if request.method == "POST":
        id_del = request.form["ingre_input_del"]
        print(id_del)

        sqliteConnection = sqlite3.connect('/Users/win/Desktop/is/butikken.db')
        cursor = sqliteConnection.cursor()
        sql_del = """DELETE FROM ingredienser WHERE idIngredienser = ?  """

        cursor.execute(sql_del,[id_del])
        sqliteConnection.commit()
        cur.close()
        return render_template ("index.html")


    return render_template("delete.html", rows = rows)


if __name__ == '__main__':
    app.run()

