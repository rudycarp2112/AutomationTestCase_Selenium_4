import mysql.connector

insertQuery="insert into city values(4080,'Cordoba','ARG','NOA',1560893)"
updateQuery="update city set Name='Neuquen' where ID=4080"
deleteQuery="delete from city where ID=4080"

#start the connections with DB (create a connection object which this python is acting as a client now we can perform some actions on DB)
try:
    con=mysql.connector.connect(host="localhost",port="3306",user="Rudy2",passwd="zinc23_._ARG",database="world")
    curs=con.cursor()
    curs.execute(deleteQuery) #we can execute other type of commands too
    con.commit()
    con.close()
except:
    print("Connection unsuccesfull...")

print("Finished")