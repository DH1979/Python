#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print(Belgium)
print(len(Belgium))
char=0
word=1
for i in Belgium:
      char=char+1
      if(i==','):
            word=word+1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)

#printed in a line
for word in Belgium:
    print("-"*len(Belgium))

belg_list = Belgium.split(",")
belg_dash = ":".join(belg_list)
print(belg_dash)

print(int(belg_list[1]) + int(belg_list[3]))

#printed in rows
#for word in Belgium:
    #print('-')


#x = Belgium.replace('word','-')
#print(x)

#std::Belgium replacetohyphen(std::Belgium phrase){
   # for(int i=0;i<(int)phrase.length();i++){
    #phrase[i]='-';}
    #return phrase;}

#x = Belgium.replace("word", "-")
#print(x)

#include <iostream>
#include <iomanip>


#[0,1,2,3,4,5,6,7,8,9]
# for i in range(0, 10):
#     print("This is iteration number " + str(i+1))
#     print(i)




