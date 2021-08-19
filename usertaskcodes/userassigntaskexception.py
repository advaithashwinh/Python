from user import userc
from task import taskc

class NotNumberError (Exception):
    def __int__(self, message):
        self.message = message

def user_to_task(USR,TASK):
    TASK.uid=USR.uid
    if USR.uid != int:
        raise NotNumberError

u1=userc("A56","Ron","weasley@xyz.com","457210")
t1=taskc(1,"Consulting",11,1,"In progress","low")

try:
    user_to_task(u1,t1)
except (NotNumberError):
    print("Invalid ID, enter digits only")
