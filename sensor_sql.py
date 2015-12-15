import sqlite3
import os

class SQL():
    def __init__(self,debug=1):
        self.debug=debug
        if not os.path.isfile('dict.sqlite'):
            self.connection=sqlite3.connect('dict.sqlite')
            self.curs = self.connection.cursor()
            cmd=('CREATE TABLE words ( "word" char(50) NOT NULL, "definition" char(500) NOT NULL,"PartOfSpeech" char(20) NOT NULL)')
            self.curs.execute(cmd)
            self.connection.commit()
            self.connection.close()

    def connect(self):
        self.connection=sqlite3.connect('dict.sqlite')
        self.curs = self.connection.cursor()

    def flush_table(self):
        self.connect()
        self.curs.execute('DELETE FROM words ')
        self.connection.commit()
        self.connection.close()

    def add_record(self,word,definition,PartOfSpeech):
        self.connect()
        self.curs.execute('INSERT INTO words VALUES ("'+word+'" , "'+definition+'", "'+PartOfSpeech+'")')
        self.connection.commit()
        self.connection.close()

    def add_verb(self,Base_Form,Past_Form,	Past_Participle_Form,S_form,Ing_Form):
        self.connect()
        self.curs.execute('INSERT INTO verbs VALUES ("'+Base_Form+'", "'+Past_Form+'", "'+Past_Participle_Form+'", "'+S_form+'", "'+Ing_Form+'")')
        self.connection.commit()
        self.connection.close()

    def raw_request(self,command):
        self.connect()
        data=[]
        try:
            for row in self.curs.execute(command):
                data.append(row)
        except:
            data='None'
        self.connection.commit()
        self.connection.close()
        return data



