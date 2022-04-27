import mysql.connector

mydb = mysql.connector.connect(
  host="mysql-db.caprover.diplomportal.dk",
  user="s205975",
  password="AchMD1mmX4asAx9DEZIDx",
  database="s205975"
)

class Database:
  def showAnmodninger(self):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Anmodninger")
    myresult = mycursor.fetchall()
    return myresult

  def addAnmodninger(self, underviser,kursus,dato,tid):
    self.underviser = underviser
    self.kursus = kursus
    self.dato = dato
    self.tid = tid
    mycursor = mydb.cursor()
    sql = "INSERT INTO Anmodninger (underviser,kursus,dato,tid) VALUES (%s, %s,%s,%s)"
    val = (underviser,kursus,dato,tid)
    mycursor.execute(sql, val)
    mydb.commit()

  def delAnmodning(self, primarykey):
    self.primarykey = primarykey
    mycursor = mydb.cursor()
    sql = f"DELETE FROM Anmodninger WHERE ID = {primarykey}"
    mycursor.execute(sql)
    mydb.commit()

  def addSkema(self, underviser,kursus,lokale,dato,tid):
    self.underviser = underviser
    self.kursus = kursus
    self.lokale = lokale
    self.dato = dato
    self.tid = tid
    mycursor = mydb.cursor()
    sql = "INSERT INTO Skema (underviser,kursus,lokale,dato,tid) VALUES (%s, %s,%s,%s,%s)"
    val = (underviser,kursus,lokale,dato,tid)
    mycursor.execute(sql, val)
    mydb.commit()

  def showSkema(self):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Skema")
    myresult = mycursor.fetchall()
    return myresult

  def getUnderviser(self, primarykey):
    self.primarykey = primarykey
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT underviser FROM Anmodninger WHERE ID = {primarykey}")
    myresult = mycursor.fetchone()
    return myresult

  def getKursus(self, primarykey):
    self.primarykey = primarykey
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT kursus FROM Anmodninger WHERE ID = {primarykey}")
    myresult = mycursor.fetchone()
    return myresult

  def getDato(self, primarykey):
    self.primarykey = primarykey
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT dato FROM Anmodninger WHERE ID = {primarykey}")
    myresult = mycursor.fetchone()
    return myresult

  def getTid(self, primarykey):
    self.primarykey = primarykey
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT tid FROM Anmodninger WHERE ID = {primarykey}")
    myresult = mycursor.fetchone()
    return myresult


