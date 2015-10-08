__author__ = 'sarahbaugh'

from script import connectToDatabase

c,db = connectToDatabase()

edges = []

for line in file("touching_mn.txt", 'r'):
    a,b = line.split(" ")
    edges.append((int(a),int(b)))

def main():
    print len(edges)
    c.executemany(
        """INSERT INTO `gerrymander`.`minnesotaTouching` VALUES (%s, %s)""",
        edges)
    db.commit()
    c.close()


if __name__ == "__main__":
    main()