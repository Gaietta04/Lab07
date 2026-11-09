from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""


class LibroDAO:
    def __init__(self):
        pass

    def get_generi(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT DISTINCT genere FROM libro ORDER BY genere")
        risultato = []
        for riga in cursor:
            risultato.append(riga[0])
        cursor.close()
        cnx.close()
        return risultato

    def get_libri_filtrati(self, biblioteca, genere):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT libro.titolo, libro.autore, libro.genere, libro.anno_pubblicazione, biblioteca.nome AS biblioteca FROM libro JOIN biblioteca ON libro.id_biblioteca = biblioteca.id
                     WHERE biblioteca.nome = COALESCE(%s, biblioteca.nome) AND libro.genere = COALESCE(%s, libro.genere)"""
        cursor.execute(query, (biblioteca, genere))
        risultato = []
        for riga in cursor:
            risultato.append(riga)
        cursor.close()
        cnx.close()
        return risultato
