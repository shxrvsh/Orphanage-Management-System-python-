import connection as con

def new(cid,name,dob,blood_group):
    con.cur.execute("insert into children values({},'{}','{}','{}')".format(cid,name,dob,blood_group))
    con.con.commit()

