import sqlite3


# class Ice:
#     def __init__(self, idIs, navn):
#         self.idIs= idIs 
#         self.navn = navn
#     def getNavn():
#         return Ice.navn
#     def getidIs():
#         return Ice.idIs
class Ice:     
    idIs=""
    navn="" 
   
   

# class forbindelse():
#     def __init__(self, idis_ingredienser, fkis,fkingredienser, mængde):
#         self.idis_ingredienser=idis_ingredienser
#         self.fkis=fkis
#         self.fkingredienser=fkingredienser
#         self.mængde=mængde
class forbindelse():
    idis_ingredienser=""
    fkis=""
    fkingredienser=""
    mængde=""
# class ingredienser () :
#     def __init__(self, idIngredienser, navn, inventar):
#         self.idIngredienser = idIngredienser 
#         self.navn = navn
#         self.inventar=inventar
class ingredienser () :
    idIngredienser = ""
    navnING=""
    inventar=""
    

def addIngrediens():
        sqliteConnection = sqlite3.connect('butikken.db')
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = """INSERT INTO ingredienser (idIngredienser, navn, inventar) VALUES  (?,?,?)"""         
        data = (str(ingredienser.idIngredienser), ingredienser.navnING, ingredienser.inventar) 
        print("row værdi: ", data)
        cursor.execute(sqlite_insert_query, data)                                                                                                                     
        sqliteConnection.commit()
        print("Record inserted successfully into ingredienser table", cursor.rowcount)
        cursor.close()

#addIngrediens()


def readIdFOR():#læs forbindelse ikke id men fkis 
    sqliteConnection = sqlite3.connect('/Users/win/Desktop/is/butikken.db')
    cursor = sqliteConnection.cursor()

    sql_select_query = """select * from forbindelse where fkis = ?""" 
    cursor.execute(sql_select_query, (forbindelse.fkis,))  
    records = cursor.fetchall()       

    print("Printing ID ", forbindelse.fkis)
    print(records)

    for row in records:                                       
        if(forbindelse.idis_ingredienser == row[0]):                  
            print("Vi har produktet")
            forbindelse.fkis = row[1]                 
            forbindelse.fkingredienser = row[2]                    
            forbindelse.mængde = row[3]  

        else:   
            print("Vi har ikke produktet")
          
                      
#readIdFOR()

def readICE():#læs Ice id 
    sqliteConnection = sqlite3.connect('/Users/win/Desktop/is/butikken.db')
    cursor = sqliteConnection.cursor()

    sql_select_query = """select * from Ice where idIs = ?""" 
    cursor.execute(sql_select_query, (Ice.idIs,))  
    records = cursor.fetchall()       

    print("Printing ID ", Ice.idIs)
    print(records)
 
    for row in records:                                       
        if( Ice.idIs == row[0]):                  
            print("Vi har produktet")
            Ice.navn = row[1]         
             
        else:   
            print("Vi har ikke produktet")
          
#readICE()



def readIdING():#læs ingredines id 
    sqliteConnection = sqlite3.connect('/Users/win/Desktop/is/butikken.db')
    cursor = sqliteConnection.cursor()

    sql_select_query = """select * from ingredienser where idIngredienser = ?""" 
    cursor.execute(sql_select_query, (ingredienser.idIngredienser,))  

    records = cursor.fetchall()       

    print("Printing ID ", ingredienser.idIngredienser)
    print(records)

    for row in records:                                       
        if(ingredienser.idIngredienser == row[0]):                  
            print("Vi har produktet")
            ingredienser.navnING = row[1]                 
            ingredienser.inventar = row[2]                    
        else:   
            print("Vi har ikke produktet")
    sqliteConnection.commit()
    sqliteConnection.close()
#readIdING()      

def update_Ice():

    sqliteConnection = sqlite3.connect('/Users/win/Desktop/is/butikken.db')
    cursor = sqliteConnection.cursor()

    cursor.execute("UPDATE  SET "
        + "navn='" + Ice.navn
        +"' WHERE idIs = '"+ Ice.idIs+"'")
    sqliteConnection.commit()        
    print(Ice.navn)


class lol():
    o = True
    
def kon():
    readICE()
    if Ice.idIs == Ice.idIs :
        update_Ice()
        print("update")

def update_ingredienser():
    con = sqlite3.connect("/Users/win/Desktop/is/butikken.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("UPDATE ingredienser SET "

        + "navnING='" + ingredienser.navnING +"' , "
        + "inventar='" + ingredienser.inventar
        +"' WHERE idIngredienser = '"+ ingredienser.idIngredienser+"'")
    con.commit()


