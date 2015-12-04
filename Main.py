from tkinter import *
import string
import random
import time

def const():
    global timer,line_counter,symbol_counter,dict,TF_width,keyboard,ascii,hh,bb,previous_pressed
    a=''
    timer=int(time.time())
    line_counter=0
    symbol_counter=0
    dict=[]
    TF_width=120
    keyboard={0:5,1:16,2:16,3:16,4:15,5:14,6:10}
    ascii={33 : '!\n1' ,34 : '"\n\'' ,35 : '#\n3' ,36 : '$\n4' ,37 : '%\n5' ,38 : '&\n7' ,39 : "\"\n'" ,
           40 : '(\n9' ,41 : ')\n0' ,42 : '*\n8' ,43 : '+\n=' ,44 : '<\n,' ,45 : '-\n_' ,46 : '>\n.' ,
           47 : '?\n/' ,48 : ')\n0' ,49 : '!\n1' ,50 : '@\n2' ,51 : '#\n3' ,52 : '$\n4' ,53 : '%\n5' ,
           54 : '^\n6' ,55 : '&\n7' ,56 : '*\n8' ,57 : '(\n9' ,58 : ':\n;' ,59 : ':\n;' ,60 : '<\n,' ,
           61 : '+\n=' ,62 : '>\n.' ,63 : '?\n/' ,64 : '@\n2' ,65 : 'A' ,66 : 'B' ,67 : 'C' ,
           68 : 'D' ,69 : 'E' ,70 : 'F' ,71 : 'G' ,72 : 'H' ,73 : 'I' ,74 : 'J' ,
           75 : 'K' ,76 : 'L' ,77 : 'M' ,78 : 'N' ,79 : 'O' ,80 : 'P' ,81 : 'Q' ,
           82 : 'R' ,83 : 'S' ,84 : 'T' ,85 : 'U' ,86 : 'V' ,87 : 'W' ,88 : 'X' ,
           89 : 'Y' ,90 : 'Z' ,91 : '{\n[' ,92 :'|\n\\' ,93 : '}\n]' ,94 : '^\n6' ,95 : '-\n_' ,
           96 : '~\n`' ,97 : 'A' ,98 : 'B' ,99 : 'C' ,100 : 'D' ,101 : 'E' ,102 : 'F' ,
           103 : 'G' ,104 : 'H' ,105 : 'I' ,106 : 'J' ,107 : 'K' ,108 : 'L' ,
           109 : 'M' ,110 : 'N' ,111 : 'O' ,112 : 'P' ,113 : 'Q' ,114 : 'R' ,115 : 'S' ,
           116 : 'T' ,117 : 'U' ,118 : 'V' ,119 : 'W' ,120 : 'X' ,121 : 'Y' ,122 : 'Z' ,
           123 : '{\n[' ,124 : '|\n\\' ,125 : '}\n]' ,126 : '~\n`',27:'',127:'',9:'',13:'',32:' ' }
    hh={33:'2_2', 34:'4_12', 35:'2_4', 36:'2_5', 37:'2_6', 38:'2_8', 39:'4_12',
        40:'2_10', 41:'2_11', 42:'2_9', 43:'2_13', 44:'5_9',45:'2_12', 46:'5_10',
        47:'5_11', 48:'2_11', 49 : '2_2', 50 : '2_3', 51 : '2_4', 52 : '2_5',
        53:'2_6', 54:'2_7', 55:'2_8', 56:'2_9', 57:'2_10', 58:'4_11', 59:'4_11',
        60:'5_9', 61:'2_13', 62:'5_10', 63:'5_11', 64:'2_3', 65:'4_2', 66:'5_6',
        67:'5_4', 68:'4_4', 69:'3_4', 70:'4_5', 71:'4_6', 72:'4_7', 73:'3_9',
        74:'4_8', 75:'4_9', 76:'4_10', 77:'5_8', 78:'5_7', 79:'3_10', 80:'3_11',
        81:'3_2', 82:'3_5', 83:'4_3', 84:'3_6', 85:'3_8', 86:'5_5', 87:'3_3',
        88:'5_3', 89:'3_7', 90:'5_2', 91:'3_12', 92:'3_14', 93:'3_13', 94:'2_7',
        95:'2_12', 96:'2_1', 97:'4_2', 98:'5_6', 99:'5_4', 100:'4_4', 101:'3_4',
        102:'4_5', 103:'4_6', 104:'4_7', 105:'3_9', 106:'4_8', 107:'4_9',
        108:'4_10', 109:'5_8', 110:'5_7', 111:'3_10', 112:'3_11', 113:'3_2',
        114:'3_5', 115:'4_3', 116:'3_6', 117:'3_8', 118:'5_5', 119:'3_3',
        120:'5_3', 121:'3_7', 122:'5_2', 123:'3_12', 124:'3_14', 125:'3_13', 126:'2_1',
        32:'6_5',9:'3_1',13:'4_13',127:'2_14',27:'1_1'}
    bb={'3_1':9,'4_13':13,'1_1':27,'6_5':32,'2_2':33,'4_12':34,'2_4':35,'2_5':36,'2_6':37,'2_8':38,'4_12':39,'2_10':40,'2_11':41,'2_9':42,'2_13':43,'5_9':44,'2_12':45,'5_10':46,'5_11':47,'2_11':48,'2_2':49,'2_3':50,'2_4':51,'2_5':52,'2_6':53,'2_7':54,'2_8':55,'2_9':56,'2_10':57,'4_11':58,'4_11':59,'5_9':60,'2_13':61,'5_10':62,'5_11':63,'2_3':64,'4_2':65,'5_6':66,'5_4':67,'4_4':68,'3_4':69,'4_5':70,'4_6':71,'4_7':72,'3_9':73,'4_8':74,'4_9':75,'4_10':76,'5_8':77,'5_7':78,'3_10':79,'3_11':80,'3_2':81,'3_5':82,'4_3':83,'3_6':84,'3_8':85,'5_5':86,'3_3':87,'5_3':88,'3_7':89,'5_2':90,'3_12':91,'3_14':92,'3_13':93,'2_7':94,'2_12':95,'2_1':96,'4_2':97,'5_6':98,'5_4':99,'4_4':100,'3_4':101,'4_5':102,'4_6':103,'4_7':104,'3_9':105,'4_8':106,'4_9':107,'4_10':108,'5_8':109,'5_7':110,'3_10':111,'3_11':112,'3_2':113,'3_5':114,'4_3':115,'3_6':116,'3_8':117,'5_5':118,'3_3':119,'5_3':120,'3_7':121,'5_2':122,'3_12':123,'3_14':124,'3_13':125,'2_1':126,'2_14':127}
    previous_pressed=''
    with open('wordsEn.txt','r') as file:
        for word in file.readlines():
            dict.append(word)
const()

def text_generator():
    global timer
    my_str=''
    while True:
        word=dict[random.randrange(0,len(dict)-2)]
        if my_str=='':#Capitalize first letter of the string
            word=word.capitalize()
        if random.randrange(0,5)==4: #Capitalize random word
            word=word.capitalize()
            if len(my_str)>1: #Dot before capitalized word
                my_str=my_str[:-2]+'.'
        if random.randrange(0,10)==7: #Coma after random word
            word=word+','
        if random.randrange(0,8)==6: #Random simbol
            word=string.punctuation[random.randrange(0,len(string.punctuation))]
        if random.randrange(0,50)==47: #Digit
            word=str(random.randrange(0,999))
        if len(my_str+' '+word)<TF_width:
            my_str=my_str+' '+word
        else:
            a=my_str.replace('\n','')[1:]
            timer=int(time.time())
            return a

def print_black():
    log['state'] = 'normal'
    log.delete(1.0,END)
    log.insert('end', line[:symbol_counter+1],'black')
    log.insert('end', line[1+symbol_counter],'green')
    log.insert('end', line[2+symbol_counter:],'grey')
    log['state'] = 'disabled'

def print_red():
    log['state'] = 'normal'
    log.delete(1.0,END)
    log.insert('end', line[:symbol_counter],'black')
    log.insert('end', line[symbol_counter],'red')
    log.insert('end', line[1+symbol_counter:],'grey')
    log['state'] = 'disabled'

def print_grey():
    log['state'] = 'normal'
    log.delete(1.0,END)
    log.insert('end', line[0],'green')
    log.insert('end', line[1:],'grey')
    log['state'] = 'disabled'

def show_keyboard(event):
    if labels['0_3'].cget('image')=='pyimage7':
        labels['0_3'].configure(image=images_pressed['0_3'])
        root.geometry('940x550')
    else:
        labels['0_3'].configure(image=images_unpressed['0_3'])
        root.geometry('940x175')

def draw_keyboard():
    global images_unpressed,images_pressed,labels
    images_unpressed={};images_pressed={};labels={}
    for row in keyboard:
        for col in range(0,keyboard[row]):
            images_unpressed[str(str(row)+'_'+str(col))]=PhotoImage(file='images/unpressed_color/Key_'+str(row)+'_'+str(col)+'.gif')
            images_pressed[str(str(row)+'_'+str(col))]=PhotoImage(file='images/pressed_color/Key_'+str(row)+'_'+str(col)+'.gif')
            if str(str(row)+'_'+str(col)) in bb.keys():
                labels[str(str(row)+'_'+str(col))]=(Label(frames['frame_'+str(row)], font=("Helvetica", 20, "normal"),text=ascii[bb[str(row)+'_'+str(col)]],compound = CENTER,padx=0,pady=0,image=images_unpressed[str(str(row)+'_'+str(col))],borderwidth=0))
            else:
                labels[str(str(row)+'_'+str(col))]=(Label(frames['frame_'+str(row)], compound = CENTER,image=images_unpressed[str(str(row)+'_'+str(col))],borderwidth=0))
            labels[str(str(row)+'_'+str(col))].grid(row=row, column=col)
    labels['0_3'].bind('<Button>',show_keyboard)

def draw_text_field():
    global log
    log = Text(frame_text, width=130, height=6,wrap='word')
    log.tag_configure("black", foreground="black",font=("Helvetica", 30, "underline"),justify='center')
    log.tag_configure("red", foreground="red",font=("Helvetica", 32),justify='center')
    log.tag_configure("grey", foreground="grey",font=("Helvetica", 30),justify='center')
    log.tag_configure("green", foreground="green",font=("Helvetica", 32),justify='center')
    log.bind('<Key>',write)
    log.grid(row=0)

def write(event):
    global symbol_counter;global line;global previous_pressed
    if previous_pressed!='':
        try:
            labels[hh[ord(previous_pressed)]].configure(font=("Helvetica", 20, "normal"),fg='black',image=images_unpressed[hh[ord(previous_pressed)]])#button img pressed
        except:
            pass
    try:
        labels[hh[ord(event.char)]].configure(font=("Helvetica", 20, "bold"),fg='red',image=images_pressed[hh[ord(event.char)]])#button img pressed
    except:
        pass
    previous_pressed=event.char
    if len(line)==symbol_counter+1:
        symbol_counter=0
        speed(line)
        line=text_generator()
        print_grey()
    else:
        if event.char not in string.whitespace or event.char==' ': #if printable
            if event.char==line[symbol_counter]:
                print_black()
                symbol_counter=symbol_counter+1
            else:
                print_red()
        else:
            pass

def speed(text):
    global timer
    if (int(time.time())-timer)>5:
        sp= int((len(text) / (int(time.time())-timer))*60)
        labels['0_1'].configure(text='       speed: '+str(sp),padx=0,pady=0,fg='DarkSlateGrey',font=("Helvetica", 16, "roman"))
        timer=int(time.time())


root = Tk()
root.geometry('940x175')
root.bind('<Key>',write)

#--------- 1 Dummy-------------
frame_dummy = Frame(root, width=10, height=25)
frame_dummy.grid()
#--------- 2 Text field ------------
frame_text = Frame(root)
frame_text.grid()
#>>>------- Keyboard frames 0-7 ------------------------
frames={}
for fr in range(0,7):
    frames['frame_'+str(fr)] = Frame(root)
    frames['frame_'+str(fr)].grid()
#---------- /Keyboard frames 0-7 --------------------<<<
root.bind('<Key>',write)
draw_keyboard()
def draw_text_field():
    global log
    log = Text(frame_text, width=130, height=6,wrap='word')
    log.tag_configure("black", foreground="black",font=("Helvetica", 30, "underline"),justify='center')
    log.tag_configure("red", foreground="red",font=("Helvetica", 32),justify='center')
    log.tag_configure("grey", foreground="grey",font=("Helvetica", 30),justify='center')
    log.tag_configure("green", foreground="green",font=("Helvetica", 32),justify='center')
    log.bind('<Key>',write)
    log.grid(row=0)
draw_text_field()
line=text_generator()
print_grey()
mainloop()