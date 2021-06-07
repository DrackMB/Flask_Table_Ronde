from flask import Flask, request, render_template
from flaskext.mysql import MySQL
import json
from datetime import datetime

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'table_ronde'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()


# Function
def insert(mysql, insertCmd, data):
    try:
        cursor.execute(insertCmd, data)
        conn.commit()
        return True
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return False


def delete(mysql, sql, data):
    try:
        cursor.execute(sql, data)
        conn.commit()
        return True
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return False


def getAll(mysql, sql):
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return False


def get(mysql, sql, data):
    try:
        cursor.execute(sql, data)
        conn.commit()
        return True
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return False


def update(mysql, sql, data):
    try:
        cursor.execute(sql, data)
        conn.commit()
        return True
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return False


@app.route('/', methods=['GET'])
def index():
    sqlQuete = """select id_quete,nom_quete from quete"""
    sqlImportance = """SELECT * FROM importance"""
    sqlEtat = """select id_etat,libelle from etats"""
    sqlExploits = """select id_exploit, nom_ex from exploit"""
    sqlChevalier = """SELECT id_chevalier,titre_chev, nom_chev,blason, reputation,quete.nom_quete, exploit.nom_ex, etats.libelle FROM chevalier  
    INNER JOIN quete,etats,exploit WHERE chevalier.id_quete = quete.id_quete AND chevalier.id_exploits = exploit.id_exploit AND chevalier.id_etat = etats.id_etat"""
    dataQuete = getAll(mysql, sqlQuete)
    dataImportance = getAll(mysql, sqlImportance)
    dataEtat = getAll(mysql, sqlEtat)
    dataExploit = getAll(mysql, sqlExploits)
    dataChevalier = getAll(mysql, sqlChevalier)

    return render_template('index.html', dataQuete=dataQuete, dataEtat=dataEtat, dataExploit=dataExploit,
                           dataChevalier=dataChevalier,dataImportance=dataImportance)


@app.route("/normal", methods=['POST'])
def recup_data_from():
    user = request.form['user']
    password = request.form['password']
    data = {"user": user, "password": password}
    sql = """INSERT INTO admin(email, password) VALUES (%(user)s, %(password)s)"""
    insert(mysql, sql, data)

    return request.form


@app.route("/addChevalier", methods=['POST'])
def send_data_chevalier():
    titre_chev = request.form['titreChevalier']
    nom_chev = request.form['nomChevalier']
    blason = request.form['Blason']
    id_quete = request.form['inputQuete']
    id_exploits = request.form['inputExploit']
    id_etat = request.form['inputEtat']
    reputation = request.form['Reputation']
    data = {"titre_chev": titre_chev, "nom_chev": nom_chev, "blason": blason, "reputation": reputation,
            "id_quete": id_quete, "id_exploits": id_exploits, "id_etat": id_etat}
    sql = """INSERT INTO chevalier(titre_chev,nom_chev, blason, reputation, id_quete, id_exploits, id_etat) 
             VALUES (%(titre_chev)s,%(nom_chev)s, %(blason)s, %(reputation)s, %(id_quete)s, %(id_exploits)s,%(id_etat)s)"""
    insert(mysql, sql, data)
    return "1"


@app.route("/addQuete", methods=['POST'])
def send_data_Quete():
    nomQuete = request.form['nomQuete']
    butQuete = request.form['butQuete']
    lieuxQuete = request.form['lieuxQuete']
    descriptifQuete = request.form['descriptifQuete']
    data = {"nom_quete": nomQuete, "but": butQuete, "lieux": lieuxQuete, "description": descriptifQuete}
    sql = """INSERT INTO quete(nom_quete, but, lieux, description) VALUES (%(nom_quete)s, %(but)s, %(lieux)s, %(description)s)"""
    insert(mysql, sql, data)
    return request.form


@app.route("/addEtat", methods=['POST'])
def send_data_Etat():
    nomEtat = request.form['nomEtat']
    data = {"Libelle": nomEtat}
    sql = """INSERT INTO etats(Libelle) VALUES (%(Libelle)s)"""
    insert(mysql, sql, data)
    return request.form


@app.route("/addImportance", methods=['POST'])
def send_data_Importance():
    nomImportance = request.form['nomImportance']
    data = {"Libelle": nomImportance}
    sql = """INSERT INTO importance(libelle) VALUES (%(Libelle)s)"""
    insert(mysql, sql, data)
    return request.form


@app.route("/addExploit", methods=['POST'])
def send_data_Exploit():
    importance = request.form['importance']
    nomExploit = request.form['nomExploit']
    data = {"nom_ex": nomExploit, "id_importance": importance}
    sql = """INSERT INTO exploit(nom_ex,id_importance) VALUES (%(nom_ex)s,%(id_importance)s)"""
    insert(mysql, sql, data)
    return request.form


@app.route("/deletChevalier", methods=['POST'])
def delete_data_Chevalier():
    idChevalier = request.form['idChevalier']
    data = (idChevalier)
    sql = """DELETE FROM `chevalier` WHERE id_chevalier=%s"""
    insert(mysql, sql, data)
    return "1"

@app.route("/updatChevalier", methods=['POST'])
def update_data_Chevalier():
    titre_chev = request.form['titreChevalierUpdate']
    nom_chev = request.form['nomChevalierUpdate']
    blason = request.form['BlasonUpdate']
    id_quete = request.form['inputQueteUpdate']
    id_exploits = request.form['inputExploitUpdate']
    id_etat = request.form['inputEtatUpdate']
    reputation = request.form['ReputationUpdate']
    idChevalier = request.form['idChevalierUpdate']
    data = {"titre_chev": titre_chev, "nom_chev": nom_chev, "blason": blason, "reputation": reputation,
            "id_quete": id_quete, "id_exploits": id_exploits, "id_etat": id_etat,"idChevalier":idChevalier}

    sql = """UPDATE chevalier 
    SET titre_chev=%(titre_chev)s,nom_chev=%(nom_chev)s,blason=%(blason)s,
    reputation=%(reputation)s,id_quete=%(id_quete)s,id_exploits=%(id_exploits)s,id_etat=%(id_etat)s 
    WHERE id_chevalier = %(idChevalier)s"""
    update(mysql, sql, data)
    return "1"



# python -m flask run -p 80 --host=0.0.0.0
