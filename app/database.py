import sqlite3
from sqlite3 import Error
import os
import pandas as pd
#http://www.sqlitetutorial.net/sqlite-python/insert/

database = "pythonsqlite.db"

phrases = [
    ('aktion1','debugge','andreas',1),
    ('aktion1','teste','andreas',1),
    ('aktion2','die Nacharbeiten','andreas',1),
    ('aktion2','den Code-Review','andreas',1),
    ('objekt','zur Zwischenschicht','andreas',1),
    ('objekt','zum Formular-Layer','andreas',1),
    ('objekt','für das Abbrechermailing','andreas',1),
    ('reason','es in der Queue hochgerutscht ist','andreas',1),
    ('reason','es in der Queue runtergerutscht ist','andreas',1),
    ('reason','es jetzt hochpriorisiert wurde','andreas',1),
    ('reason','es jetzt runterpriorisiert wurde','andreas',1),
    ('nachsatz','An der Stelle.','andreas',1),
    ('nachsatz','Und dann schaue ich was noch in der Queue liegt.','andreas',1),
    ('nachsatz','Habe ich Peakwork gesakt??.','andreas',1),
    ('nachsatz','Und halte mich ansonsten bereit.','andreas',1),
    ('nachsatz','Und den Rest hab ich vergessen.','andreas',1)
]

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_phrase(conn, phrases):
    """
    Create a new project into the projects table
    :param conn:
    :param phrases:
    :return: project id
    """
    for phrase in phrases:
        sql = """ INSERT INTO phrases(position, phrase, author, active)
                  VALUES('{}','{}','{}',{}) """.format(phrase[0],phrase[1],phrase[2],phrase[3])
        cur = conn.cursor()
        cur.execute(sql)
    return cur.lastrowid


def initialize_db(database=database, phrases=phrases):
    if not os.path.isfile(database):
        sql_create_table_phrases = """ CREATE TABLE IF NOT EXISTS phrases (
                                            id integer PRIMARY KEY,
                                            position text NOT NULL,
                                            phrase text,
                                            author text,
                                            active integer
                                        ); """

        conn = create_connection(database)
        if conn is not None:
            create_table(conn, sql_create_table_phrases)
            with conn:
                # create a new phrase
                phrase_id = insert_phrase(conn, phrases)
                print(phrase_id)
        else:
            print("Error! cannot create the database connection.")
    else:
        return

def query_db(database):
    conn = create_connection(database)
    if conn is not None:
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT position, phrase, author, active FROM phrases")
            rows = cur.fetchall()
            df = pd.DataFrame(rows, columns=["position", "phrase", "author", "active"])
            df = df[df["active"] == 1]
            return df
