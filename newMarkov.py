#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict 
import random

#f = open('Holmes.txt','r');
#f = open('MountainMadness.txt','r')
#f = open('KJVBible.txt','r');
f = open('dump.txt','r');
text = f.read();

dictWords = defaultdict(list); 
ngram = None;

specialReplace = "\n";
banned="\"\'«\t";
capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
numbers = "1234567890"

def clean(text, banned):
    for char in banned:
        text = text.replace(char,"");
    for char in specialReplace:
        text = text.replace(char," ");
    for i in range(5):
        text.replace("  "," ");
    return text

def ngram(size):
    global text;
    for i in range(len(text)-size):
        #print(text[i:i+size]+" Guess: "+text[i+size]);
        dictWords[text[i:i+size]].append(text[i+size]);

def getNext(current):
    if len(current) != 0:
        out = (random.sample(dictWords[current],1));
        if (out == " " and current == " "):
            getNext(current);
        return out;
    else:
        temp = (random.sample(dictWords.keys(),1)[0]);
        while((temp[0] not in capitals)): #capitals
            temp = (random.sample(dictWords.keys(),1)[0]);

        return temp;

def itterativeNext(start, X):
    global period;
    i = 0;
    origin = start;
    while (len(start) < X and not condition(".!?",start,period)):
        temp = start[i:i+size];
        temp = getNext(temp);
        start = start+temp[0];
        i=i+1;

    if (condition("!?.",start,period)):
        return start;
    else:
        return itterativeNext(origin,X);

def condition(symbols, text, cap):
    cnt = 0;
    for item in symbols:
        cnt=cnt+text.count(item);

    return cnt >= cap;


def findStart(start):
    text = start;
    while (text != "."):
        text = getNext(text);
    while (text != " "):
        text = getNext(text);

    return text; 

size = 0;
period = 3;
text = clean(text,banned);

for i in range(10):
    try:
        size = random.randint(6,8)+2;
        ngram(size);
        start = itterativeNext(getNext(""),280);
      
        print(str(size)+": "+clean(start,banned)+"\n");
    except:
       pass
f.close()    
