class Compiler_Project:
    def CountArtiles(self,x):
        count=0
        article=[]
        for k in x:
          if (k=='a' or k=='A') or (k=='a' or k=='A') or (k=='an' or k=='An') or (k=='the' or k=='The'):
            count+=1
            article.append(k)
        return count,article

    def Auxiliary_Verb(self,x):
        v=['am','Am','is','Is','are','Are','was','Was','were','Were','been','have','Have','Has','has','Had','had','Shall','shall','Will','will',
           'can','Can','Could','could','Would','would','May','may','Might','might']
        count1=0
        Av=[]
        for i in x:
            if v.count(i):
                count1+=1
                Av.append(i)
        return count1,Av

    def Count_Prepositions(self,x):
        preposition=['about','above','across','after','against','along','among','around','as','at','before','behind','between','by','during','except',
                    'for','from','in','like','next','of','off','on','over', 'past','than','through','to','until', 'up','with,within']
        count2=0
        p=[]
        for k in x:
            if preposition.count(k):
                count2+=1
                p.append(k)
        return count2,p

    def RemoveExtraSpace(self,x):
        print("After removing extra space:", end=" ")
        for i in x:
            print(i,end=" ")

    def Find_Valid_Identifier(self,x):
        valid=[]
        count1=0
        for str in x:
            count = 0
            if ((str[0]>='a' and str[0]<='z') or (str[0]>= 'A' and str[0]<= 'Z') or str[0]== '_'):
                  count+=1
                  for i in range(1,self.Length_Of_String(str)):
                        if ((str[i]>='a' and str[i]<='z') or (str[i]>='A' and str[i]<='Z') or (str[i]>= '0' and str[i]<='9') or (str[i] == '_')):
                                count+=1
            if (count==self.Length_Of_String(str)):
                valid.append(str)
                count1+=1
        return count1,valid

    def Find_Invalid_Identifier(self,x):
        valid=self.Find_Valid_Identifier(x)
        count=0
        Invalid=[]
        for k in x:
            if valid[1].count(k)==0:
                count+=1
                Invalid.append(k)
        return count,Invalid



    def StrongVerb(self,x):
        S_verb=['beat', 'beaten', 'become', 'became', 'begin', 'began', 'begun', 'bend', 'bent', 'bet', 'bid', 'bite', 'bit', 'bitten', 'blow','blew','pays',
        'blown', 'break', 'broke', 'broken','bring', 'brought', 'build', 'built', 'burn', 'burned', 'burnt', 'burnt', 'buy', 'bought', 'bought','works','runs',
        'catch', 'caught', 'caught', 'choose', 'chose', 'chosen','come', 'came', 'cost', 'cost', 'cost', 'cut', 'cut', 'cut', 'dig', 'dug', 'dive','work','sits',
        'dove', 'dived', 'do', 'did', 'done', 'draw', 'drew','dream', 'dreamt', 'dreamed', 'drive', 'drove', 'driven', 'drink', 'drank', 'drunk', 'eat','eats',
        'ate', 'eaten', 'fall', 'fell', 'fallen','feel', 'felt', 'felt', 'fight', 'fought', 'fought', 'find', 'found', 'found', 'fly', 'flew', 'flown','holds',
        'forget', 'forgot', 'forgotten', 'forgive', 'forgave', 'forgiven', 'freeze', 'froze', 'frozen', 'get', 'got', 'gotten', 'give', 'gave', 'given','rises',
        'go', 'went', 'gone', 'grow','hang', 'hung','hear', 'heard', 'hide', 'hid', 'hidden', 'hit', 'hold', 'held', 'hurt', 'keep','bets','bits','blows','loses'
        'kept', 'know', 'knew', 'known', 'lay', 'laid', 'laid', 'lead', 'led', 'leave', 'left', 'lend', 'lent', 'let', 'lie', 'lay', 'lain', 'lose','brings','solve',
        'lost', 'make', 'made', 'mean', 'meant', 'meet', 'met', 'pay', 'paid', 'put', 'read', 'ride', 'rode', 'ridden','ring', 'rang', 'rung', 'rise','love','solved'
        'rose', 'risen', 'ran', 'run', 'say', 'said', 'see', 'saw', 'seen', 'sell', 'sold', 'send', 'sent', 'show', 'showed', 'shown', 'shut', 'sing','loves','solves'
        'sang', 'sung', 'sit', 'sat', 'sleep', 'slept', 'speak', 'spoke', 'spoken', 'spend', 'spent', 'stand', 'stood', 'swim', 'swam', 'swum', 'take','loved',
        'took', 'taken', 'teach', 'taught', 'tear', 'tore', 'torn', 'tell', 'told', 'told', 'think', 'thought', 'throw', 'threw', 'thrown', 'understand','brings'
        'understood', 'wake', 'woke', 'woken', 'wear', 'wore', 'worn', 'win', 'won', 'won', 'write', 'wrote', 'written','comes','writes','meets','feels','leaves'
        'shows','forgets','goes','eats','means','tears','sleeps','teaches','wins','tells','drives','breaks','becomes','builds','burns','comes','falls','does',
        'forgets','draws','sings','fights','dreams','catches','lays','blows','costs','cuts','buys','drinks','hears','chooses','gets','wears','makes','knows']

        count12=0
        verb=[]
        for v in x:
            if S_verb.count(v):
                count12+=1
                verb.append(v)
        print("Number of strong/week verbs:",count12,end=" ")
        return verb

    def CountAll(self,x):
        vowel=0
        consonant=0
        space=0
        digit=0
        for i in range(self.Length_Of_String(x)):
            if x[i]=='a' or x[i]=='A' or x[i]=='e' or x[i]=='E' or x[i]=='I' or x[i]=='i' or x[i]=='o' or x[i]=='O' or x[i]=='u' or x[i]=='U':
                vowel+=1
            elif x[i]>='0' and x[i]<='9':
                digit+=1
            elif x[i]==' ':
                space+=1
            else:
                consonant+=1

        print(" Number vowels:",vowel,'\n',"Number of consonants:",consonant,'\n',"number of digits:",digit,'\n',"Number of words:",space+1,'\n',"Number of space:",space,'\n')

    def Length_Of_String(self,x):
        lenn=0
        for i in x:
            lenn+=1
        return lenn

    def ReverseString(self,x):
        return x[::-1]

    def CountNo_Of_Sentence(self,x):
        lines = 0
        for k in range(self.Length_Of_String(x)):
            if x[k] == '.':
                lines += 1
        return lines

    def SearchItem(self,x,s):
        for i in x:
            if i==s:
                return True
        return False

    def RemoveingItem(self,x,word):
        for i in x:
            if i==word:
                x.remove(i)
                return x
        else:
            return 0

    def Maximum_Frequency_of_a_String(self,x):
        maxx = 0
        for i in x:
            if maxx < x.count(i):
                maxx = x.count(i)
                p = i
        return maxx,p


#I am Golam Rabbani . I love python progr@mming very much python python . I haved solved more than 300 problems in differnt online judge . #Rana is a good    boy  2020 python

lst=Compiler_Project()
x=input("Enter a string:")
print()
while True:
    print("1.Show the string\n2.Tokenize the string\n3.Number of article\n4.Number of Auxiliary verb\n5.Number of prepositions\n6.Remove Extra space")
    print("7.Find valid identifier from the given string\n8.Find Invalid Identifier\n9.Number of strong/week verbs\n10.Count vowel,consonant,digits,white_space,word")
    print("11.Show length of the string\n12.Reverse the string\n13.Count number of sentence\n14.Search an item from the string\n15.Remove a word\n16.Maximum frequency of a word\n0.Exit\n")
    n=int(input("Chose your option:"))

    if n==1:
        print("The input string is:",x,'\n')

    elif n==2:
        print("After tokenization the string:",x.split(),'\n')

    elif n==3:
       print("Number of articles:",lst.CountArtiles(x.split()),'\n')

    elif n==4:
      print("Number of Auxiliary verb:",lst.Auxiliary_Verb(x.split()),'\n')

    elif n==5:
        print("The number of prepositions:",lst.Count_Prepositions(x.split()),'\n')

    elif n==6:
        lst.RemoveExtraSpace(x.split())
        print('\n')
    elif n==7:
        print("The valid identifiers from the string:",lst.Find_Valid_Identifier(x.split()),'\n')

    elif n==8:
        print("The invalid identifiers from the string:", lst.Find_Invalid_Identifier(x.split()), '\n')

    elif n==9:
        print(lst.StrongVerb(x.split()),'\n')

    elif n==10:
        lst.CountAll(x)

    elif n==11:
        print("Length of the given string:",lst.Length_Of_String(x),'\n')

    elif n==12:
        print("The reversed string:",lst.ReverseString(x),'\n')

    elif n==13:
        print("The no of Sentence:",lst.CountNo_Of_Sentence(x),'\n')

    elif n==14:
        while True:
           ch=input("Do you want to search(Y/N):")
           if ch.upper()=='Y':
               s=input("Enter search item:")
               if lst.SearchItem(x.split(),s):
                    print(s," is present in the given string\n")

               else:
                 print("Sorry! ",s," is not present in the given string\n")
           else:
               break

    elif n==15:
        while True:
            ch=input("Do you want to remove(Y/N):")
            if ch.upper()=='Y':
               word=input("Enter removing item:")
               print("After removing the word,The string looks like:",end=" ")
               p=lst.RemoveingItem(x.split(),word)
               if p:
                   for k in p:
                      print(k,end=" ")
                   print()
               else:
                   print("Sorry! ",word," is not present in the string")

            else:
                break

    elif n==16:
        print("Maximum frequency and word",lst.Maximum_Frequency_of_a_String(x.split()))

    elif n==0:
        break