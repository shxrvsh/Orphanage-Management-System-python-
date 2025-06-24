import connection as con
from datetime import date

def adopt(cid,contact,date_exit):
    con.cur.execute("select * from children where id={}".format(cid))
    data=con.cur.fetchone()
    con.cur.execute("insert into adoption values({},'{}','{}','{}','{}','{}')".format(data[0],data[1],data[2],data[3],date_exit,contact))
    con.cur.execute("delete from children where id={}".format(cid))
    con.con.commit()
adopt(1,'8608669977','2023-05-04')

