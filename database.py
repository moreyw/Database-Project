
import _mysql

with open("config.conf", 'r') as file:
    host, user, passwd, db = file.read().split()
    
db=_mysql.connect(host=host,user=user, passwd=passwd, db=db)
