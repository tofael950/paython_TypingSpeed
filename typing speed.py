words=['ability','able','about','above','accept','according','account','across',
'act','action','activity','actually','add','address','administration',
'admit','adult','affect','after','again','against','age','agency',
'agent','ago','agree','agreement','ahead','air','all','allow','almost','alone',
'along','already','also','although','always','American','among','amount',
'analysis','and','animal','another','answer','any','anyone','anything','appear',
'apply','approach','area','argue','arm','around','arrive','art','article',
'artist','as','ask','assume','at','attack','attention','attorney','audience',
'author','authority','available','avoid','away','baby','back','bad','bag','ball',
'bank','bar','base','be','beat','beautiful','because','become','bed','before',
'begin','behavior','behind','believe','benefit','best','better','between',
'beyond','big','bill','billion','bit','black','blood','blue','board','body',
'book','born','both','box','boy','break','bring','brother','budget','build',
'building','business','but','buy','by','call','camera','campaign','can','cancer',
'candidate','capital','car','card','care','career','carry','case','catch',
'cause','cell','center','central','century','certain','certainly','chair',
'challenge','chance','change','character','charge','check','child','choice',
'choose','church','citizen','city','civil','claim','class','clear','clearly',
'close','coach','cold','collection','college','color','come','commercial',
'common','community','company','compare','computer','concern','condition',
'conference','Congress','consider','consumer','contain','continue','control',
'cost','could','country','couple','course','court','cover','create','crime',
'cultural','culture','cup','current','customer','cut',
'dark','data','daughter','day','dead','deal','death','debate','decade','decide',
'decision','deep','defense','degree','Democrat','democratic','describe','design',
'despite','detail','determine','develop','development','die','difference',
'different','difficult','dinner','direction','director','discover','discuss',
'discussion','disease','do','doctor','dog','door','down','draw','dream','drive',
'drop','drug','during',
'each','early','east','easy','eat','economic','economy','edge','education',
'effect','effort','eight','either','election','else','employee','end','energy',
'enjoy','enough','enter','entire','environment','environmental','especially',
'establish','even','evening','event','ever','every','everybody','everyone',
'everything','evidence','exactly','example','executive','exist','expect',
'experience','expert','explain','eye',
'face','fact','factor','fail','fall','family','far','fast','father','fear',
'federal','feel','feeling','few','field','fight','figure','fill','film','final',
'finally','financial','find','fine','finger','finish','fire','firm','first',
'fish','five','floor','fly','focus','follow','food','foot','for','force',
'foreign','forget','form','former','forward','four','free','friend',
'from','front','full','fund','future',
'game','garden','gas','general','generation','get','girl','give','glass','go',
'goal','good','government','great','green','ground','group','grow','growth',
'guess','gun','guy',
'hair','half','hand','hang','happen','happy','hard','have','he','head','health',
'hear','heart','heat','heavy','help','her','here','herself','high','him',
'himself','his','history','hit','hold','home','hope','hospital','hot','hotel',
'hour','house','how','however','huge','human','hundred','husband',
'idea','identify','if','image','imagine','impact','important','improve','in',
'include','including','increase','indeed','indicate','individual','industry',
'information','inside','instead','institution','interest','interesting',
'international','interview','into','investment','involve','issue',
'it','item','its','itself','job','join','just','keep','key','kid','kill','kind',
'kitchen','know','knowledge','land','language','large','last','late','later',
'laugh','law','lawyer','lay','lead','leader','learn','least','leave','left',
'leg','legal','less','let','letter','level','lie','life','light','like','likely',
'line','list','listen','little','live','local','long','look','lose','loss',
'lot','love','low',
'machine','magazine','main','maintain','major','majority','make','man','manage',
'management','manager','many','market','marriage','material','matter','may',
'maybe','me','mean','measure','media','medical','meet','meeting','member',
'memory','mention','message','method','middle','might','military','million',
'mind','minute','miss','mission','model','modern','moment','money','month',
'more','morning','most','mother','mouth','move','movement','movie','much','music',
'must','myself','name',
'nation','national','natural','nature','near','nearly','necessary','need',
'network','never','new','news','newspaper','next','nice','night','no','none',
'nor','north','not','note','nothing','notice','now','number',
'occur','off','offer','office','officer','official','often',
'oil','old','on','once','one','only','onto','open','operation','opportunity',
'option','or','order','organization','other','our','out','outside','over',
'own','owner','page','pain','Painting','paper','parent',
'part','participant','particular','particularly','partner','party',
'pass','past','patient','pattern','pay','peace','people','per','perform',
'performance','perhaps','period','person','personal','phone','political',
'politics','poor','popular','population','position','positive','possible',
'power','quite','race','radio',
'raise','range','rate','rather','reach','read','ready','real','reality','realize',
'really','reason','receive','recent','recently','recognize','record','red',
'reduce','reflect','region','relate','relationship','religious','remain',
'remember','remove','report','represent','Republican','require','research',
'resource','respond','response','responsibility','run','safe','same','save',
'say','scene','school','science','scientist','score','sea','season','seat',
'second','section','security','see','seek','seem','sell','send','senior','sense',
'series','serious','serve','service',
'set','seven','several','shake','share','she','shoot','short','shot','should',
'shoulder','show','side','sign','significant','similar','simple','simply','since',
'sing','single','sister','sit','site','situation','six','size','skill','skin',
'small','smile',
'so','social','society','soldier','some','somebody','someone','something',
'sometimes','speech','spend','sport','spring','staff','stage','stand','standard',
'star','start','state','statement','station','stay','step','still','stock',
'stop','store','story','strategy','street','strong','structure','student','study',
'stuff','style','subject','success','successful','such','suddenly','suffer',
'suggest','summer','support','sure','surface','system','table','take','talk',
'task','tax','teach','teacher','team','technology','television','tell','ten',
'tend','term','test','than','thank','thing','think','third','this','those',
'though','thought','thousand','threat','three','through','throughout','throw',
'thus','time','to','today','together','tonight','too','top','total','tough',
'toward','town','trade','traditional','training','travel','treat','treatment',
'tree','trial','trip','trouble','true','truth','try','turn','TV','two','type',
'under','understand','unit','until','up','upon','us','use','usually','value',
'various','very','victim','view','violence','visit','voice','vote','wait',
'weapon','wear','week','weight','well','west','western','what','whatever',
'when','where','whether','whose','why','wide','wife','will','win','wind',
'window','wish','with','within','without','woman','wonder','word','work',
'worker','world','worry','would','write','writer','wrong','yard',
'yeah','year','yes','yet','you','young','your','yourself']



def slider():
    global count,sliderwords
    text='Welcome to Typing Speed Increaser'
    if count>= len(text):
        count =0
        sliderwords =''
    sliderwords += text[count]
    count +=1
    fontlabel.configure(text=sliderwords)
    fontlabel.after(150,slider)


def time():
    global timer,score,miss
    if timer>11:
        pass
    else:
        timerlabelcount.configure(fg='red')
    if timer>0:
        timer -=1
        timerlabelcount.configure(text=timer)
        timerlabelcount.after(1000,time)
    else:
        gameinstruction.configure(text='Hit = {} | Miss = {} | Total Score = {}'
                                  .format(score,miss,score-miss))
        rr= messagebox.askretrycancel('Notification','Wanna Play Again!!!!')
        if rr==True:
            score=0
            miss=0
            timer=60
            timerlabelcount.configure(text=timer)
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)
            wordentry.delete(0, END)

def startgame(event):
    global score, miss
    if timer==60:
        time()
    gameinstruction.configure(text='')
    startlabel.configure(text='')
    if wordentry.get()== wordlabel['text']:
        score +=1
        scorelabelcount.configure(text=score)
    else:
        miss +=1
    random.shuffle(words)
    wordlabel.configure(text=words[0])
    wordentry.delete(0,END)

from tkinter import *
import random
from tkinter import messagebox

###############################################
root= Tk()
root.geometry('800x600+400+100')
root.configure(bg='black')
root.title('Typing Speed Increaser')


##############################################

score=0
miss=0
timer=60
count=0
sliderwords=''

#################################################################
fontlabel=Label(root,text='',font=('airal',25,
                'italic bold'),bg='black',fg='purple',width=40)
fontlabel.place(x=10,y=10)
slider()


startlabel=Label(root,text='Lets begin!!!',font=('airal',30,
                  'italic bold'),bg='black',fg='white')
startlabel.place(x=275,y=50)

random.shuffle(words)
wordlabel=Label(root,text=words[0],font=('airal',45,
                'italic bold'),bg='black',fg='green')
wordlabel.place(x=350,y=240)


scorelabel=Label(root,text='Your Score:',font=('arial',25,
                'italic bold'),bg='black',fg='red')
scorelabel.place(x=10,y=100)

scorelabelcount=Label(root,text=score,font=('arial',25,
                'italic bold'),bg='black',fg='blue')
scorelabelcount.place(x=150,y=180)



timerlabel=Label(root,text='Time Left:',font=('arial',25,
                'italic bold'),bg='black',fg='red')
timerlabel.place(x=600,y=100)

timerlabelcount=Label(root,text=timer,font=('arial',25,
                'italic bold'),bg='black',fg='blue')
timerlabelcount.place(x=600,y=180)



gameinstruction= Label(root,text='Type the Word and hit enter button',
                       font=('arial',25,'italic bold'),bg='black',fg='grey')
gameinstruction.place(x=150,y=500)

########################################################################

wordentry= Entry(root,font=('airal',25,'italic bold'),bd=10,justify='center')
wordentry.place(x=250,y=330)
wordentry.focus_set()

#################################################################
root.bind('<Return>',startgame)
root.mainloop()