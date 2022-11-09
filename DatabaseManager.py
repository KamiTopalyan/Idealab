import mysql.connector

connection = mysql.connector.connect(host='192.168.1.22',
                                     port=3306,
                                     user="remoteRoot",
                                     password='768519',
                                     database='Idealab')

cursor = connection.cursor()


def Insert(ID, name, count, date):
    sql = "INSERT INTO Stock (ItemID, Name, Count, lastChange) VALUES (%s, %s, %s, %s)"
    val = (ID, name, count, date)
    cursor.execute(sql, val)
    connection.commit()
    print(cursor.rowcount, "record inserted.")


def getColumn():
    sql = "SELECT * FROM Stock"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

