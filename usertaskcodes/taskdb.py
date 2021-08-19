from datetime import datetime
import mysql.connector
from task import taskc

def connectToDB():
        mydb = mysql.connector.connect(host="localhost", user="root", password="alpha11a2h", database="python")
        return mydb

def insertTask(task):
        mydb = connectToDB()
        mycursor = mydb.cursor()
        sql = "insert into task (taskid,name,descr,status,priority,ownerid,creatorid,createdon,modifiedon) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (task.tid,task.tname,task.des,task.status,task.tprio,task.oid,task.cid,task.crtdon,task.mdfdon)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()

t = taskc("5","Meeting","Summary of week","Upcoming","1","45","34",datetime.now(),datetime.now())
insertTask(t)

