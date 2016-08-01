import os
import re
import sys
import math
import codecs
import pickle
#words=[]


#mainfilepath = "C:/Users/AKANKSHA/Desktop/catalan_corpus_train_tagged.txt"
mainfilepath=sys.argv[1]

def readTags_word():
    wordspart = []
    word_tag_list = {}
    tag_count = {}
    taglist=list()

    tag = ""
    tagcount={}
    two_tags_count={}
    Transition_prob={}
    Emission_prob={}
    linecount=0
    #f1 = codecs.open("C:/Users/AKANKSHA/Desktop/tags.txt", 'w')

    f= codecs.open(mainfilepath,'r')

    str_read=f.read()
    for line in str_read.split("\n"):
        prevTag = "StartTag"
        endTag="End"

        linecount=linecount+1
        for words in line.split():
            #wordx=""

            wordIndex=len(words)
            wordx=words[0:wordIndex-3]
            tag=words[wordIndex-2:]
            if tag not in taglist:
                taglist.append(tag)
            tagcount[tag]=tagcount.get(tag,0)+1
            tag_tag_list=0


            two_tags_count[prevTag,tag]=two_tags_count.get((prevTag,tag),0)+1
            words_count=0
            word_tag_list[wordx, tag] = word_tag_list.get((wordx, tag), 0) + 1


            prevTag=tag

        two_tags_count[tag, endTag] = two_tags_count.get((tag, endTag), 0) + 1






    tagcount["StartTag"]=linecount
    tagcount["End"]=linecount

    #print two_tags_count




    #print word_tag_list
    #print tagcount

    #print two_tags_count

    for key,val in two_tags_count.items():
        #if tagcount.get(key[0]) is not 0 and val is not None and tagcount.get(key[0]) is not None:
        Transition_prob[key]=float((float)(val)/(float)(tagcount.get(key[0])))


    #print prob

    ccccc=0
    eeeee=0

    for key,val in word_tag_list.items():
        Emission_prob[key]=float((float)(val)/(float)(tagcount.get(key[1])))

    file1= open("hmmmodel.txt",'w')
    pickle.dump(Transition_prob,file1)
    # print Emission_prob
    # print Transition_prob
    # print taglist
    # for key, val in Transition_prob.items():
    # file1.write(str(key[0])+ ' ' + str(key[1])+ ' ' + str(val)+ ';')
    pickle.dump(Emission_prob,file1)
    pickle.dump(taglist,file1)
    pickle.dump(tagcount,file1)
    file1.close()

    #file1.write("&&&& ")
    #for key, val in Emission_prob.items():
        #file1.write(str(key[0])+ ' '+ str(key[1])+ ' '+ str(val)+ ';')







        #words.append(line.split(" "))
        #print words



    #for item in words:
        #f1.write("%s\n" % item)
  #  for i in range(0,words.__len__()):

   #         f1.write(words[i])





readTags_word()






