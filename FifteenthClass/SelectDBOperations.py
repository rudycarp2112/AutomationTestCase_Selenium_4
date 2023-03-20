import mysql

selectQuery="select * from city where ID>4076"

#start the connections with DB (create a connection object which this python is acting as a client now we can perform some actions on DB)
try:
    con= mysql.connector.connect(host="localhost", port="3306", user="Rudy2", passwd="zinc23_._ARG", database="world")
    curs=con.cursor() # curs is an temporaly buffer that saved the data from DB
    curs.execute(selectQuery) #we can execute other type of commands too
    # con.commit() --> commit its not required because we dont use transaction commands to apply any change to an object of DB

    for row in curs:
        print("First field: " + str(row[0]) + "; Second Field: " + row[1] + "; Third Field: " + row[2])
    con.close()
except:
    print("Connection unsuccesfull...")

print("Finished")