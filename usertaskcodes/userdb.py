from datetime import datetime
import mysql.connector
from user import userc

def connectToDB():
        mydb = mysql.connector.connect(host="localhost", user="root", password="alpha11a2h", database="python")
        return mydb

def insertUser(user):
        mydb = connectToDB()
        mycursor = mydb.cursor()
        sql = "insert into user (username,contactno,role,dob,createdon,modifiedon) values(%s,%s,%s,%s,%s,%s)"
        val = (user.uname,user.phone,user.role,user.dob,user.cretdon,user.mdfdon)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()

u = userc(5,"Advaith","9696969696","TTS",datetime.now(),datetime.now(),datetime.now())
insertUser(u)