#choose 8 random precincts and put them in a list
import MySQLdb




def connectToDatabase():
    db = MySQLdb.connect(host="45.79.146.49", # your host, usually localhost
                         user="root", # your username
                          passwd="correcthorsewhatever", # your password
                          db="gerrymander") # name of the data base

    cur = db.cursor()

    return cur



def beginProcess(cur):
    pList = cur.execute("SELECT column FROM table ORDER BY RAND()LIMIT 8")
    for precinct in pList:
        addNeighbor(precinct)





#def addNeigbor(precinct):
    #if(precinct.hasNeigbors()):

cur = connectToDatabase()
item = cur.execute("SELECT OID_ FROM minnesota ORDER BY RAND()")
print item
