import mysql.connector as mc

con=mc.connect(host="localhost",user='root',passwd="19122004",database='orphanage')

def close():
    con.close()

