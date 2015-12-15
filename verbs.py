import requests
import json

from sensor_sql import SQL
sql=SQL()


with open('verbs.txt','r') as file:
    a=file.readlines()
counter=1
for chunk in a:
    chunk=chunk.rstrip()
    x = [i for i in chunk.split()]
    #print (x)
    Base_Form=x[1]
    Past_Form=x[2]
    Past_Participle_Form=x[3]
    S_form=x[4]
    Ing_Form=x[5]
    sql.add_verb(Base_Form,
                 Past_Form,
                 Past_Participle_Form,
                 S_form,
                 Ing_Form)

    print (counter,
    Base_Form,
    Past_Form,
    Past_Participle_Form,
    S_form,
    Ing_Form,'\n')
    counter+=1