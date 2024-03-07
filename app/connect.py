import cx_Oracle

username = 'SYSTEM'
password = 'admin'
host = 'localhost'
port = '1521'
service_name = 'XE'

dsn = cx_Oracle.makedsn(host, port, service_name)

connection = cx_Oracle.connect(username, password, dsn)

cursor = connection.cursor()