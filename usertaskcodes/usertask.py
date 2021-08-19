from task import taskc
from user import userc

def user_to_task(USR,TASK):
    isint=True
    try:
        int(USR.uid)
    except ValueError:
        isint=False
    if isint:
        TASK.uid=USR.uid
    else:
        print("Wrong data type")

u1=userc(22,"Ash","ashton@xyz.com","2430000")
t1=taskc(1,"Meeting",12,21,"In progress","high")

user_to_task(u1,t1)
print(t1.uid)
print(t1.tname)
print(t1.status)
print(t1.dstart)
print(t1.dend)
print(t1.tprio)

u2=userc("A56","Ron","weasley@xyz.com","457210")
t2=taskc(1,"Consulting",11,1,"In progress","low")

user_to_task(u2,t2)

