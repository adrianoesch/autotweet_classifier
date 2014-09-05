from collections import Counter
import re
import sys
import numpy as np
from termcolor import colored
import os

def getPosFreq(tweetlist):
    cnt=Counter()
    for tweet in tweetlist:
        words = re.split(' |\t',tweet)
        wordpos=[]
        for word in words:
          wordpos.append((word,words.index(word)))
        cnt.update(wordpos)
    return cnt.items(), sum(cnt.values()),cnt.most_common(len(tweetlist)/3)

def getMeanAndStdFreq(word,cntr):
    list=[]
    for i in range(0,len(cntr)):
        if word == cntr[i][0][0]:
          list.append(cntr[i][1])
    return np.mean(list), np.std(list)

def getEvals(x,tlist):
  poslist = [tlist[i][0][0] for i in range(0,len(tlist))]
  eva={}
  for i in range(0,len(x)):
    m,s = getMeanAndStdFreq(x[i][0][0],tlist)
    if s!=0:
      eva[x[i][0]]=((x[i][1]-m)/s)+(m/s)
    else:
      eva[x[i][0]]=x[i][1]
  return eva

def compare(lines,eva):
  for l in lines:
    scoreli=[]
    words = re.split(' |\t',l)
    for w in words:
      try:
        scoreli.append(eva[(w,words.index(w))])
      except:
        bla=0
    lscore=sum(scoreli)/len(words)
    if lscore>2.8:
      print colored( str(round(lscore))+'\t'+l.encode('utf-8'),'red')
    else:
      print str(round(lscore))+'\t'+l.encode('utf-8')


def classify(lines):
  tlist,ovsum,x = getPosFreq(lines)
  eva = getEvals(x,tlist)
  compare(lines,eva)
