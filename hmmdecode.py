#coding: utf-8
import pickle
import re
import sys
import math
import codecs

file2=open("hmmmodel.txt",'r')
read_transition=pickle.load(file2)
read_emission=pickle.load(file2)
read_taglist=pickle.load(file2)

prob_trans={}
prob_emiss={}

for key,val in read_transition.items():
    if key[0] in prob_trans:
        prob_trans[key[0]][key[1]]=val
    else:
        prob_trans[key[0]]={}
        prob_trans[key[0]][key[1]]=val

for key,val in read_emission.items():
    if key[0] in prob_emiss:
        prob_emiss[key[0]][key[1]]=val
    else:
        prob_emiss[key[0]]={}
        prob_emiss[key[0]][key[1]]=val








#mainfilepath = "C:/Users/AKANKSHA/Desktop/catalan_corpus_dev_raw.txt"
mainfilepath=sys.argv[1]

back_pointer={}

hmmoutput={}

def viterbi_algo():
    # viterbi={}
    OutputStringStore = ""
    f = open(mainfilepath, 'r')
    file3=open("hmmoutput.txt",'w')
    counterr=0
    str = f.read()
    #ccc=0
    for line in str.split("\n"):
        # line="A part de l' Hostalnou_de_Bianya , Llocalou , i la Vall_de_el_Bac , el municipi comprèn , a més , el poble de Capsec , que fins el 1917 donà nom a el municipi , i una sèrie d' antics llocs i parròquies , algunes d' origen romànic , que havien pertangut a els distints monestirs propers ( Riudaura , Camprodon , Sant_Pere_de_Besalú , Sant_Joan_les_Fonts , Sant_Joan_de_les_Abadesses ) : Santa_Margarida_de_Bianya , Sant_Pere_Despuig , Sant_Martí_de_Bianya ( o de Solamal ) i Sant_Martí_de_el_Clot ( o de Tornadissa ) , a la vall de Bianya ; Porreres , Llongarriu , Sant_Feliu_de_el_Bac , Sant_Miquel_de_la_Torre i Santa_Magdalena_de_el_Coll , a la vall de el Bac ; el poble i castell de Castellar_de_la_Muntanya , a la vall de Castellar , i el terme separat de la Canya ."
        # if ccc==60:
        #     break
        # ccc=1+ccc
        #linecount = linecount + 1
        viterbi={}
        words=line.split(" ")

        localstr = ""
        firstword_taglist=[]
        current_word_tag = []
        prev_word_tag = []
        listloop = []

        if words[0] in prob_emiss:
            firstword_taglist=prob_emiss[words[0]].keys()
        else:
            firstword_taglist=read_taglist


        for stag in firstword_taglist:
            if words[0] in prob_emiss:
                prob_value_emiss=float(prob_emiss[words[0]].get(stag,0.00004))
            else:
                prob_value_emiss=0.00004
            viterbi[stag, 0]=float(prob_value_emiss*float(prob_trans["StartTag"].get(stag,0.00004)))


        for t in range(1,words.__len__()):


            if words[t] in prob_emiss and prob_emiss[words[t]].keys()>0:
                current_word_tag=prob_emiss[words[t]].keys()
            else:
                current_word_tag=read_taglist

            for i in current_word_tag:
                max=-100000.0
                if words[t-1] in prob_emiss and prob_emiss[words[t-1]].keys()>0:
                    prev_word_tag=prob_emiss[words[t-1]].keys()
                else:
                    prev_word_tag=read_taglist

                best_state=""

                for stag in prev_word_tag:
                    # print viterbi.get((s,t-1),0.00004)

                    c_trans=0.00004
                    b_emiss=0.00004
                    d=0.00005
                    a_viterbi=float(viterbi.get((stag,t-1),0.00004))

                    if words[t] in prob_emiss:
                        b_emiss=float(prob_emiss[words[t]].get((i),0.00004))
                    else:
                        b_emiss=0.00004

                        #print b_emiss
                    # print b_emiss
                    if stag in prob_trans:
                        c_trans=float(prob_trans[stag].get((i),0.00004))
                    else:
                        c_trans=0.00004

                    # print b_emiss

                    d=float(float(a_viterbi)*float(b_emiss)*float(c_trans))

                    if max<=d:
                        viterbi[i,t]=d
                        #print viterbi[1,t]
                        if viterbi[i, t] == 0:
                            viterbi[i, t] = 0.1
                        max = viterbi[i, t]

                        best_state=stag
                back_pointer[i,t]=best_state

        if words[words.__len__()-1] in prob_emiss and prob_emiss[words[words.__len__()-1]].keys()>0:
            listloop=prob_emiss[words[words.__len__()-1]].keys()
        else:
            listloop=read_taglist
        for tag in listloop:
            maxp=0.0
            itr1=0.00004
            itr2=0.00004
            if tag in prob_trans:
                itr1=float(prob_trans[tag].get("End",0.00004))
            else:
                itr1=.00004
            itr2=viterbi.get((tag,words.__len__()-1),0.00004)
            finali=float(itr1*itr2)
            if finali>=maxp:
                back_pointer["End",words.__len__()]=tag
                maxp=finali
        len_word=words.__len__()
        finalstate="End"
       # print counterr
        #counterr=counterr+1



        while len_word>0:
 #           print back_pointer[finalstate, j]

            finalword=(words[len_word-1])


            finalstate = back_pointer[finalstate, len_word]

            localstr=finalword+"/"+finalstate+" "+localstr

            len_word=len_word-1
        if OutputStringStore=='':
            ##stringstore
            OutputStringStore=localstr
            ###456789
        else:
            OutputStringStore=OutputStringStore+"\n"+localstr ##21313


    file3.write(OutputStringStore)
viterbi_algo()



