import requests
import json
import time
from sensor_sql import SQL
sql=SQL()


with open('dict_10.txt','r') as file:
    a=file.readlines()
counter=1
for word in a:
    word=word.rstrip()

    if_exist=sql.raw_request('SELECT word FROM words WHERE word="'+word+'"')
    if if_exist==[]:
        try:
            url='http://dictionaryapi.net/api/definition/'+word
        except:
            pass
        else:
            b=requests.get(url).text

            try:
                c=json.loads(b)

            except:
                pass
            else:
                try:
                    definition=(c[0]['Definitions'][0])
                    definition=definition.replace('"','')
                    definition=definition.replace("'",'')
                    definition=definition.replace('`','')
                    PartOfSpeech=(c[0]['PartOfSpeech'])
                except:
                    print ('except')
                else:
                    print(counter,'\n', word, '\n',definition, '\n',PartOfSpeech)
                    sql.add_record(word, definition, PartOfSpeech)
                    time.sleep(.5)
    else:
        print(counter,'Word exists - no action')
    counter+=1
