from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT nome FROM biblioteca ORDER BY nome")
        risultato = []
        for riga in cursor:
            risultato.append(riga[0])
        cursor.close()
        cnx.close()
        return risultato
