#!/usr/bin/env python3
import json
import pyodbc

with open('docs/cred.json','r') as f:
    c = json.load(f)

def connect():

    conn = pyodbc.connect(
        Driver = '{ODBC Driver 17 for SQL Server}',
        Server = c['srv'],
        Port = c['prt'],
        Database = c['db'],
        Trusted_Connection = 'no',
        UID = c['uid'],
        PWD = c['pwd']
        )

    try:
        conn
        print('Database Connection Successful...')

    except pyodbc.Error as e:
        status = e.args[1]
        print(status) 

    finally:
        return conn
