#remove empty list from a list
list1=[89,[],84,1,2,[],5,[],6]
list2=[]
for i in list1:
    if i!=[]:
        list2.append(i)
        
    else:
        continue
print(list2)

#Remove all the duplicates a word in a sentence
sentence="big black bug bit a big black dog on his big black nose"
s2=sentence.split()
l=[]
for i in s2:
    if i not in l:
        l.append(i)
       
s3=' '.join(l)
print(s3)
#All the occuraces of a character in a given list
string=input("enter a string")
count=0
ele=input("enter a character to get count")
for i in string:
    if i == ele:
        count+=1
print("Count is=",count)