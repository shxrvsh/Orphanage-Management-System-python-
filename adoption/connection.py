import mysql.connector as mc

con=mc.connect(host="localhost",user='root',passwd="19122004",database='orphanage')
cur=con.cursor()
def close():
    con.close()

