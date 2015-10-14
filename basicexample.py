__author__ = 'sarahbaugh'
from Node import Node
from script import connectToDatabase

c,db = connectToDatabase()
c2 = c
c.execute("SELECT ALL OID_, USH_RVOTE_, USH_DVOTE_ FROM minnesota")

nodes = []
j = 0
for (OID_, USH_RVOTE_, USH_DVOTE_) in c:

    nodes.append(Node)
    x = USH_RVOTE_
    y = USH_DVOTE_
    z = OID_
    print "repub"  + str(x), "dem" + str(y)
    nodes[j].votes = int(float(x)) + int(float(y))
    nodes[j].id = z

    print "VOTES" + str(nodes[j].votes)
    c2.execute("SELECT p2  FROM minnesotaTouching WHERE p1 = " + str(z))
    neighborlist =  []
    for p2 in c2:
        nodes[j].touching.append(p2)
    nodes[j].touching.append("done")
    j= j + 1





def main():
    i = 0
    while i < 1:
        print 'hi!'
        i = i + 1
    print "length is", len(nodes)
    print nodes[0].votes
    print nodes[1].touching

    db.commit()
    c.close()


if __name__ == "__main__":
    main()