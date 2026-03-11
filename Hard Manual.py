import random
import time

print("Preparing Wordlist...")
words=open("Wordle Solutions.txt").read().splitlines()
yellows=[[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']]
greens=[' ',' ',' ',' ',' ']
blacks=[]
alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
grades=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
openers=open("Top Openers.txt").read().splitlines()
vocabulary=open("dictionary.txt").read().splitlines()



def sliceoff(arr,el):
    r=len(arr)
    for i in range(r):
        if(arr[i]==el):
            relist=arr[:i]+arr[(i+1):]
            return relist
    else: return arr

def noblacks(blacks,wordlist):
    words=wordlist
    for i in wordlist:
        for j in blacks:
            if j in i:
                words=sliceoff(words,i)
                break
    return (words)

def greenword(greens,wordlist):
    words=wordlist
    for j in range(5):
        if(greens[j]!=" "):
            for i in words:
                if greens[j]!=i[j]:
                    words=sliceoff(words,i)
    return words

def yellowing(yellows,wordlist):
    words=wordlist
    for i in yellows:
        for j in range(5):
            if i[j]!=' ':
                for k in words:
                    if i[j] in k:
                        if i[j]==k[j]: words=sliceoff(words,k)
                    else: words=sliceoff(words,k)
    return words

def try_nore(wordlist):
    words=wordlist
    for i in wordlist:
        for j in i:
            nl=0
            for k in i:
                if j==k: nl+=1
            if nl>1:
                words=sliceoff(words,i)
                break
    if len(words)>0: return words
    else: return wordlist

def slot(yellow,chr):
    for i in range(5):
        if chr in yellow[i]: return i
    else:
        for j in range(5):
            for k in yellow[j]:
                if k!=" ": break
            else: return j

def shortlist(green,yellow,black,words):
    words=noblacks(black,words)
    words=yellowing(yellow,words)
    words=greenword(green,words)
    return words

def printarr(arr):
    for i in range(len(arr)):
        print(arr[i]+",",end=" ")
    print('...')

def mark(i):
    marks=input(">>> ")
    if not len(marks) == 5:
        print("Wrong Input!")
        marks=mark(i)
    for l in marks:
        if l not in "012":
            print("Wrong Input!")
            marks=mark(i)
            break
    return marks

def grade():
    for i in range(26):
        freq=0
        for j in words:
            if alphabets[i] in j:
                freq+=1
        presence=round((freq/len(words))*100)
        if presence>50: points=100-presence
        else: points=presence
        grades[i]=points

def AddnCut(n,arr):
    for i in range(10):
        if n>arr[i]:
            temp=arr[i]
            arr[i]=n
            for k in range(9-i):
                j=k+i+1
                temp+=arr[j]
                arr[j]=temp-arr[j]
                temp-=arr[j]
            break
    else: return arr,'none'
    return arr,i

def place(ele,pos,arr):
    temp=arr[pos:9]
    arr[pos]=ele
    for i in range(len(temp)):
        arr[pos+1+i]=temp[i]
    return arr

def bestword(words):
    bestgrade=[0,0,0,0,0,0,0,0,0,0]
    best_word=["","","","","","","","","",""]
    for i in words:
        marks=0
        for j in range(26):
            if alphabets[j] in i:
                marks+=grades[j]
        bestgrade,pos=AddnCut(marks,bestgrade)
        if pos!='none':
            best_word=place(i,pos,best_word)
    for j in best_word:
        if j=="": best_word=sliceoff(best_word,j)
    return best_word

def trial(word,marks):
    yellows=[[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']]
    greens=[' ',' ',' ',' ',' ']
    blacks=[]
    for j in range(5):
        if marks[j]=='0':
            blacks+=[word[j]]
        elif marks[j]=='2':
            greens[j]=word[j]
        elif marks[j]=='1':
            row=slot(yellows,word[j])
            yellows[row][j]=word[j]
    return blacks,yellows,greens

def most_suitable(choices):
    bestword=[]
    bestgrade=2309
    for word in choices:
        total_possibilities=0
        for l1 in range(3):
            for l2 in range(3):
                for l3 in range(3):
                    for l4 in range(3):
                        for l5 in range(3):
                            marks=str(l1)+str(l2)+str(l3)+str(l4)+str(l5)
                            b,y,g=trial(word,marks)
                            remsol=len(shortlist(g,y,b,words))
                            total_possibilities+=remsol*round((remsol/2309)*100)
        avg=total_possibilities/100
        if(avg<bestgrade):
            bestgrade=avg
            bestword=[word]
        elif(avg==bestgrade):
            bestword.append(word)
    return bestword

def trigger():
    time.sleep(0)

word=random.choice(openers)
for i in range(2309):
    print("The available words are",end=" ")
    printarr(words)
    print("#%d: %s" %(i+1,word))
    time.sleep(1.25)
    marks=mark(i)
    print("\n")
    if marks=="22222":
        congrats=["GENIUS!","MAGNIFICENT!","IMPRESSIVE!","SPLENDID!","GREAT!","PHEW!"]
        print(congrats[i])
        break
    for j in range(5):
        if(j==0): position='1st'
        elif(j==1): position='2nd'
        elif(j==2): position='3rd'
        elif(j==3): position='4th'
        else: position='5th'
        if marks[j]=='0':
            blacks+=[word[j]]
            print("\'{0}\' is not in the word.".format(word[j]))
        elif marks[j]=='2':
            greens[j]=word[j]
            print("\'{0}\' is the {1} letter of the word.".format(word[j],position))
        elif marks[j]=='1':
            row=slot(yellows,word[j])
            yellows[row][j]=word[j]
            print("\'{0}\' is in the word but is not the {1} letter of the word.".format(word[j],position))
    print("\n")
    if(i != 2308):
        words=shortlist(greens,yellows,blacks,words)
        vocabulary=shortlist(greens,yellows,blacks,vocabulary)
        grade()
        choices=bestword(vocabulary)
        print(choices)
        if len(words)==1: word=words[0]
        elif len(words)>10: word=random.choice(try_nore(most_suitable(choices)))
        else: word=random.choice(try_nore(most_suitable(choices+words)))
