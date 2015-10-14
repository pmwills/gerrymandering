__author__ = 'sarahbaugh'
from Node import Node
from script import connectToDatabase

c, db = connectToDatabase()
c2, db = connectToDatabase()
c.execute("SELECT ALL OID_, USH_RVOTE_, USH_DVOTE_ FROM minnesota")

nodes = []
for (OID_, USH_RVOTE_, USH_DVOTE_) in c:
    # print "repub"  + str(x), "dem" + str(y), "z" + str(z)

    #print "VOTES" + str(nodes[j].votes)
    c2.execute("SELECT p2 FROM minnesotaTouching WHERE p1 = " + str(OID_))
    touching = [x for x in c2]
    id = OID_
    votes = int(USH_RVOTE_) + int(USH_DVOTE_)
    newNode = Node(id, touching, votes)
    nodes.append(newNode)


def main():
    i = 0
    while i < 1:
        print 'hi!'
        i = i + 1
    print "length is", len(nodes)
    print nodes

    db.commit()
    c.close()


if __name__ == "__main__":
    main()