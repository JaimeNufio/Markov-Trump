import string
import json
import time
import random
from collections import defaultdict

theDict = defaultdict(list);
data = [];

def prepareText(text):
    
    text = text.lower();
    exclude = set(string.punctuation+"\n");
#    text = ''.join(ch for ch in text if ch not in exclude);
    text = text.split(' ');
    return text;

def parseJSON():
    with open('Trump.json') as data_file:
        jsonInfo = json.load(data_file);
    return jsonInfo

def stepThroughJSON():
    jsonTxt = parseJSON();
    for i in range(len(jsonTxt)):
       stepThroughText(jsonTxt[i]['text']);


def twoGram(someArray,index):
    thing = (someArray[index],someArray[index+1]);
    return thing;

def stepThroughText(text):
    global theDict, intro
    text = prepareText(text);
    skip = False
    for word in text:
        if "//" in word:
            skip = True
    
    if not skip:
        for i in range(len(text)-1):
            thePair = twoGram(text,i);
            data.append(thePair);   

def dataToDict():
    for one, two in data:
        theDict[one].append(two);

def getWord():
    global theDict;
    return random.choice(theDict.keys());

def getNextWord(word):
    global theDict;
    #print(word);
    #print(word[len(word)-1]);
    if len(theDict[word]) < 1:# or word[len(word)-1] in ".!?":# or word[0] == "#":
        x = random.random(); y = random.random();
        if x < y:
            word = getWord(); #Lack an entry with current word, fetch random word
        else:
            word = "";
    else:
        lst = theDict[word];
       # print("The Word:"+word)
        lst = random.choice(lst)
       # print("Chose: "+lst);
        return lst;
    return (word);

def check(snippet, currentLen):
    

    if len(snippet) < 1:
        return False;
    
    if currentLen > 100:    #only consider if over 100 char
        if snippet[len(snippet)-1] == '.': 
         #   print("Has Period.");
            return False;
        if snippet[0] == "#":
         #   print("Has Hashtag.");
            return False;
        if currentLen+len(snippet) > 135: #140 is our hard limit
         #   print("Exceeding cap.");
            return False;
#    print('passed check');
    return True

def fixEnd(text):
    words = text.split(" ");
    punctuation = ["!",".",".",".",".",".",".","?"];
    for i in range(len(words)-1,0,-1):
        
        #print(words[i]);

        if 0 < 1:
            break;

        if len(words[i]) > 1:
            if "#" in words[i]:
#                print("found hashtag");
                pass;
            if "." not in words[i]:
                words[i] = words[i]+random.choice(punctuation);
 #               print("added punc:"+words[i]);
                break;
            if "." in words[i] or "!" in words[i] or "?" in words[i]:
  #              print("was fine");
                break;  #lets not worry if we found punctuation
    newTxt = "";
    for word in words:
        newTxt=newTxt+word+" ";

   # print(len(newTxt));
    return newTxt;
                
def tweet():
    total = "";
    while True: #CANT STOP WONT STOP
        theWord = getWord(); #The seed, I guess you'd call it
        total = theWord;
        nextWord = "";
        contTweet = True;
        while contTweet:
            theWord = getNextWord(theWord);
            if check(theWord,len(total)):
                total = total+" "+theWord;
            else:
                contTweet = False;

        time.sleep(1.5);
        print(fixEnd(total)+" "+str(len(fixEnd((total)))));
        contTweet = True

def oldTweet():
    total = ""
    maxCnt = 5;
    while True:
        theWord = getWord();
        total = theWord;
        while len(total) < 120 and theWord != "":# or containCount(total,"!?.") > maxCnt:
            got = getNextWord(theWord);
            total = total+" "+got;
            theWord = getNextWord(got);
            total = total+" "+theWord;
        time.sleep(1);
        print(total)
        total = "";

def feed(word):
    
    total = ""
    maxCnt = 5;
    charLimit = 250;
    theWord = word;
    total = theWord;
    while len(total) < charLimit:# or containCount(total,"!?.") < maxCnt:
        got = getNextWord(theWord);
        total = total+" "+got;
        theWord = getNextWord(got);
        total = total+" "+theWord;
    print(total)

def containCount(text,symbols):
    count = 0;
    for char in text:
        for sym in symbols:
            if char == sym:
                count=count+1;
    return count;

#test = ("ARE OMFG, ARE WE ARE REALLY ARE DOING THIS AGAIN?? ARE WE REALLY DOING THIS AGAIN OMG");
#print(stepThroughText("ARE OMFG, ARE WE ARE REALLY ARE DOING THIS AGAIN?? ARE WE REALLY DOING THIS AGAIN OMG"));


test ="""
Oh my god,
Are we doing this again?
Are we really doing this again?
Oh my god,
I just can't believe
We really can be doing this again.
Oh, we never learn.
Oh, we never ever learn.
Will we ever learn?
Tell me something,
Or can you be sure.
That the next time we
Head for the door,
That you'll go your way,
And I'll go mine.
'Cause I keep on doing this
All of the time with you
Again and again
And again and again.
Again and again.
Oh my god,
Are we doing this again?
Are we really doing this again?
Oh my god.
Switch off those eyes, oh,
'Cause they show.
You are to happen,
I already know.
You're my worst habit
I'm trying to break.
If you keep giving,
I'll probably take from you.
Again and again and again and again
Again and again.
Oh my god,
Are we doing this again?
Are we really doing this again?
Oh my god,
I just can't believe
We really can be doing this again.
Will we ever learn?
Will we never ever ever learn.
Do you wanna learn?
What the hell were we thinking?
I think we all
Should probably start thinking,
And then things will not go so far.
Try to keep our distance.
Try to take some time.
Try to see things clearly,
And get you the hell off my mind.
Oh my god,
Are we doing this again?
Are we really doing this again?
Oh my god,
I just can't believe
We really can be doing this again.
Will we never learn?
Will we never ever learn?
We're never gonna learn.
"""

"""
print(theDict);
txt = (getWord());
while True:
    print(txt);
    txt = getNextWord(txt);
    print(txt)
"""

stepThroughJSON();
dataToDict();

#for i in range(100):
#    print(fixEnd("This is a test"));

#print(fixEnd("This is another. test"));

tweet()


