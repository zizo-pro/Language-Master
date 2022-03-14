import mysql.connector
db = mysql.connector.connect(
  host = "localhost",
  user = "ziad",
  passwd = "@zizo2412@",
  database = "german_database"
)
cr = db.cursor()

typ = input("word type: ")

if typ.upper() == "NOUN":
	word = input("Noun: ").capitalize()
	article = input("Artikle: ").capitalize()
	meaning = input("Bedeutung: ").capitalize()
	plural = input("Plural: ").capitalize()
	category = input("Kategorie: ").capitalize()
	example = input("Beispiel: ").capitalize()
	cr.execute("INSERT INTO nouns (article,noun,meaning,type,plural,category,example) VALUES (%s,%s,%s,%s,%s,%s,%s)",(article,word,meaning,typ.capitalize(),plural,category,example))

elif typ.upper() == "VERB":
	word = input("Verb: ").capitalize()
	perfect = input("Perfect: ").capitalize()
	meaning = input("Bedeutung: ").capitalize()
	status = input("Verb Status: ").capitalize()
	aux_verb = input("Hilfsverb: ").capitalize()
	example = input("Beispiel: ").capitalize()
	cr.execute("INSERT INTO verbs (verb,perfect,meaning,type,status,auxiliary_verb,example) VALUES (%s,%s,%s,%s,%s,%s,%s)",(word,perfect,meaning,typ.capitalize(),status,aux_verb,example))

elif typ.upper() == "ADJ":
	word = input("Adjektiv: ").capitalize()
	meaning = input("Bedeutung: ").capitalize()
	male = input("männlich: ").capitalize()
	female = input("weiblich: ").capitalize()
	neutral = input("Neutral: ").capitalize()
	example = input("Beispiel : ").capitalize()
	cr.execute("INSERT INTO adjectives (adjective,meaning,male,female,neutral,type,example) VALUES (%s,%s,%s,%s,%s,%s,%s)",(word,meaning,male,female,neutral,"Adjective",example))
Q1 = "CREATE TABLE adjectives (adjective VARCHAR(50) NOT NULL,meaning VARCHAR(40) NOT NULL,male VARCHAR(40) NOT NULL, female VARCHAR(40) NOT NULL,neutral VARCHAR(40) NOT NULL, type VARCHAR(15) NOT NULL, example VARCHAR(100) NOT NULL,ID int PRIMARY KEY AUTO_INCREMENT)"
# cr.execute(Q1)
# cr.execute("SELECT * FROM nouns")

# data = cr.fetchall()
# for i in data:
# 	print(i)

db.commit()